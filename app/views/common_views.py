from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from django.shortcuts import redirect, render

from django.conf import settings

from django.db.models import *

from app.models.invoice_model import *
from app.models.collects_model import *
from app.models.items_model import *
from app.models.users_model import *
from app.models.contacts_model import *

from app.forms.invoice_forms import *
from app.forms.items_form import *
from app.forms.contact_forms import *
from app.forms.tax_form import *

from app.other_constants import country_list

import json


#**********************************************************************************************
# FETCH CONTACT BILLING/SHIPPING ADDRESSES 
#**********************************************************************************************
#

def fetch_contact_addresses(request, ins=None):

    data = {'ret':0, 'organization_name':'', 'addresses':{}}

    if ins is not None:

        try:
            contact = Contacts.objects.get(pk = int(ins))
        except:
            return HttpResponse(json.dumps(data))

        contact_addresses = Contact_Addresses.objects.filter(contact = contact).values('contact_person', 
            'flat_no', 'street', 'city', 'state', 'country', 'pincode', 'is_billing_address', 
            'is_shipping_address')
        
        data['ret'] = 1
        data['organization_name'] = contact.organization_name
        data['addresses'] = list(contact_addresses)        

        return HttpResponse(json.dumps(data))
    return HttpResponse(json.dumps(data))


#**********************************************************************************************
# FETCH CONTACT BILLING/SHIPPING ADDRESSES 
#**********************************************************************************************
#

def fetch_products(request):
    products = ProductsModel.objects.filter(user = request.user).values()
    return HttpResponse(json.dumps(products))

def fetch_products_dropdown(request):
    products = ProductsModel.objects.filter(user = request.user).values('id', 'product_name')
    
    html = ['<option></option>']

    for row in products:
        html.append('<option id="{}">{}</option>'.format(row["id"], row["product_name"]))

    return HttpResponse(''.join(html))


#**********************************************************************************************
# FETCH CONTACT BILLING/SHIPPING ADDRESSES 
#**********************************************************************************************
#

def fetch_product_details(request, ins=None):
    data = {'ret':0, 'details':{}, 'quantity_in_stock':0}

    if ins is not None:
        
        product = ProductsModel.objects.filter(pk = int(ins)).values()
        data['details'] = list(product)
        
        p_count = InventoryProduct.objects.filter(product = product[0]["id"]).aggregate(total = Sum('quantity'))
        data['quantity_in_stock'] = p_count["total"]     
        data['product_type'] = items_constant.PRODUCT_TYPE_DICT[product[0]["product_type"]]   

        return HttpResponse(json.dumps(data))
    return HttpResponse(json.dumps(data))


#**********************************************************************************************
# FETCH CONTACT BILLING/SHIPPING ADDRESSES 
#**********************************************************************************************
#

def add_contact_or_employee(request):

    if request.POST:
        contact_form = ContactsForm(request.POST)
        tax_form = TaxForm(request.POST)        
        contact_address_form_1 = ContactsAddressForm(request.POST, prefix = 'form1')
        contact_address_form_2 = ContactsAddressForm(request.POST, prefix = 'form2')
        contact_account_details_form = ContactAccountDetailsForm(request.POST)

        ins = None

        if contact_form.is_valid():
            ins = contact_form_ins = contact_form.save(commit = False)
            contact_form_ins.user = request.user

            if contact_form_ins.is_imported_user:
                try:
                    profile = Profile.objects.get(app_id__iexact = contact_form_ins.app_id)
                    imp_user = User.objects.get(pk = profile.user_id)
                except:
                    return redirect('/unauthorized/', permanent = False)
                
                contact_form_ins.imported_user = imp_user
            
            social_form = ContactsExtraForm(request.POST, request.FILES, instance = contact_form_ins)
            if social_form.is_valid():
                social_form.save()

            contact_form_ins.save() 

        if ins is not None:
            #
            # tax form save
            if tax_form.is_valid(): 
                obj_tax = tax_form.save(commit = False)
                obj_tax.contact = ins

                other_details_form = OtherDetailsForm(request.POST, instance = obj_tax)
                if other_details_form.is_valid():
                    other_details_form.save()
                obj_tax.save()    
            else:
                pass

            #
            # contact_account_details_form save
            if contact_account_details_form.is_valid():
                obj_acc = contact_account_details_form.save(commit = False)
                obj_acc.contact = ins
                obj_acc.save() 
            else:
                pass
            
            #
            # address form save
            if contact_address_form_1.is_valid():
                obj_add1 = contact_address_form_1.save(commit = False)
                obj_add1.contact = ins
                obj_add1.save() 
            else:
                pass

            #
            # address 2 form save
            if contact_address_form_2.is_valid():
                x = request.POST.get("more_address_table_enabled", None)
                if x == '1' and x is not None:
                    obj_add2 = contact_address_form_2.save(commit = False)
                    obj_add2.contact = ins
                    obj_add2.save() 
            else:
                pass

        return redirect(request.META.get('HTTP_REFERER'), permanent = False)
    return redirect('/unauthorized/', permanent = False)
    