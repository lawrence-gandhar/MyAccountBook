from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.invoice_model import *
from app.models.collects_model import *
from app.forms.invoice_forms import *

from app.other_constants import country_list

import json

#=====================================================================================
#   CONTACT - INVOICE LIST
#=====================================================================================
#
class Invoice(View):

    # Template 
    template_name = 'app/app_files/invoice/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["active_link"] = 'Invoice'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    def get(self, request):
        return render(request, self.template_name, self.data)

#=====================================================================================
#   DESIGN INVOICE
#=====================================================================================
#
class InvoiceDesigner(View):
    # Template 
    template_name = 'app/app_files/invoice/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["active_link"] = 'Invoice'
    data["included_template"] = 'app/app_files/invoice/template_design_form.html'
    data["breadcrumb_title"] = 'INVOICE DESIGNER'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/design_template.js']
  
    def get(self, request, *args, **kwargs):

        #
        #   USER PHONE LIST
        #
        records = Profile.objects.filter(user = self.request.user)
            
        phone_records = records.values('official_phone', 'personal_phone', 'alternative_phone')    
        PHONE_NUMBERS = []
        for i in phone_records:
            for x in i: 
                if i[x] is not None:
                    PHONE_NUMBERS.append((x,i[x]))
        self.data["PHONE_NUMBERS"] = (tuple(PHONE_NUMBERS))

        #
        #   USER EMAIL ADDRESSES
        #
        email_records = records.values('official_email', 'personal_email') 
        EMAILS = []
        for i in email_records:
            for x in i: 
                if i[x] is not None:
                    EMAILS.append((x,i[x]))
        self.data["EMAILS"] = (tuple(EMAILS))

        #
        #   USER BILLING ADDRESSES
        #
        #billing_addresses = User_Address_Details


        self.data["invoice_design_form"] = InvoiceDesignerForm(request.user)
        return render(request, self.template_name, self.data)

    def post(self, request, *args, **kwargs):
        form = InvoiceDesignerForm(request.user, request.POST, request.FILES or None)
        print(form.errors)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()
            return redirect('/invoice/invoice_designer/manage/', permanent = True)
        return render(request, self.template_name, self.data)    

#=====================================================================================
#   BASE - CREATE INVOICE
#=====================================================================================
#

def manage_invoice_designs(request):
    
    # Template 
    template_name = 'app/app_files/invoice/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["active_link"] = 'Invoice'
    data["included_template"] = 'app/app_files/invoice/manage_invoice_designs.html'
    data["breadcrumb_title"] = 'INVOICE DESIGNER'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    data["designs"] = Invoice_Templates.objects.filter(user = request.user)

    return render(request, template_name, data)


#=====================================================================================
#   BASE - CREATE INVOICE
#=====================================================================================
#
class CreateInvoice(View):
    
    # Initialize 
    data = defaultdict()
    
    # Template 
    template_name = 'app/app_files/invoice/create_invoice.html'
    data["included_template"] = 'app/app_files/invoice/template_design_form.html'

    # Set link as active in menubar
    data["active_link"] = 'Invoice'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data['js_files'] = []

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)

#=====================================================================================
#   CONTACT - CREATE INVOICE
#=====================================================================================
#
class CreateContactInvoice(View):
    
    # Initialize 
    data = defaultdict()
    
    # Template 
    template_name = 'app/app_files/invoice/create_invoice.html'
    data["included_template"] = 'app/app_files/invoice/template_design_form.html'

    # Set link as active in menubar
    data["active_link"] = 'Invoice'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data['js_files'] = ['custom_files/js/design_template.js']

    # Initialize Forms
    data["invoice_template_design_form"] = ''

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)


#=====================================================================================
#   COLLECTIONS - CREATE INVOICE
#=====================================================================================
#
class CreateCollectionInvoice(View):
    
    # Initialize 
    data = defaultdict()
    
    # Template 
    template_name = 'app/app_files/invoice/create_invoice.html'
    data["included_template"] = 'app/app_files/invoice/create_collection_invoice_form.html'

    # Set link as active in menubar
    data["active_link"] = 'Invoice'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data['js_files'] = ['custom_files/js/design_template.js']

    #
    #
    #
    def get(self, request, *args, **kwargs):

        ins = int(self.kwargs['ins'])

        inv = Invoice_Templates.objects.filter(user = request.user)
        inv_details = inv.values()[0]

        #
        # Profile & Address Details
        #

        profile = Profile.objects.get(user = request.user)

        #
        # USER - FIRSTNAME & LASTNAME
        #
        self.data["template_username"] = ""

        if inv_details["user_display_name"]:
            self.data["template_username"] = request.user.first_name.upper()+" "+request.user.last_name.upper()
        else:
            self.data["template_username"] = inv_details["user_custom_name"]

        #
        # EMAIL ON TEMPLATE
        #
        self.data["template_email"] = ""

        if inv_details["user_email"] is not None:
            if inv_details["user_email"] == 'official_email':
                self.data["template_email"] = profile.official_email
            else:
                self.data["template_email"] = profile.personal_email
        else:
            if request.user.email is not None: 
                self.data["template_email"] = request.user.email   

        self.data["invoice_templates"] = inv.values('id', 'template_name')

        try:
            collect = Collections.objects.get(pk = ins)
        except:
            return redirect('/unauthorized/', permanent = True)

        #
        # PHONE ON TEMPLATE
        #
        self.data["template_phone"] = ""

        if inv_details["user_phone"] is not None:
            if inv_details["user_phone"] == 'official_phone':
                self.data["template_phone"] = profile.official_phone
            else:
                self.data["template_phone"] = profile.personal_phone

        #
        # BILLING ADDRESS OF USER ON THE TEMPLATE 
        #
        self.data["user_billing_address"] = []

        if inv_details["billing_address_id"] is not None:
            
            try:
                billing_address = User_Address_Details.objects.get(user = request.user, pk = inv_details["billing_address_id"])
                self.data["user_billing_address"].append(billing_address.flat_no)
                self.data["user_billing_address"].append(billing_address.street)
                self.data["user_billing_address"].append(billing_address.city+" - "+billing_address.pincode)
                self.data["user_billing_address"].append(billing_address.state)
                self.data["user_billing_address"].append(country_list.COUNTRIES_LIST_DICT[billing_address.country])
            except:    
                pass

            self.data["user_billing_address"] = ',<br>'.join(self.data["user_billing_address"]).upper()


        self.data["contact_details"] = Contacts.objects.get(pk = collect.contact.id)
        self.data["collections"] = collect
        self.data["partial_collections"] = CollectPartial.objects.filter(collect_part = collect)
        
        return render(request, self.template_name, self.data)

    #
    # 
    #     
    def post(self, request, *args, **kwargs):
        ins = int(self.kwargs['ins'])

