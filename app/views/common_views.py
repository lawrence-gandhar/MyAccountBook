from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from django.conf import settings

from django.db.models import *

from app.models.invoice_model import *
from app.models.collects_model import *
from app.models.items_model import *
from app.models.users_model import *
from app.models.contacts_model import *

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