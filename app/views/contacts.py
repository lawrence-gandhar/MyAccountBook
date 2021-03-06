from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import *
from app.models.users_model import *
from app.forms.contact_forms import *
from app.forms.tax_form import *
from app.forms.inc_fomsets import *

from django.conf import *

from django.db import *
from django.db.models import Q


import json, os, csv, re

#=====================================================================================
#   CONTACTS VIEW
#=====================================================================================
#
class ContactsView(View):

    # Template 
    template_name = 'app/app_files/contacts/base.html'
    
    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["contacts"] = {}
    data["active_link"] = 'Contacts'
    data["breadcrumb_title"] = 'CONTACTS'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    data["included_template"] = 'app/app_files/contacts/view_contacts.html'
    
    #
    #
    def get(self, request):        

        search = request.GET.get('search',False)

        contacts = contacts_model.Contacts.objects.filter(user = request.user)

        if search:
            contacts = contacts.filter(
                Q(contact_name__contains = search) | 
                Q(display_name__contains = search) |
                Q(organization_name__contains = search)
            )

        self.data["contacts"] = contacts
        
        return render(request, self.template_name, self.data)


#=====================================================================================
#   ADD CONTACTS
#=====================================================================================
#
def add_contacts(request, slug = None, ins = None):

    # Initialize 
    data = defaultdict()

    # Template 
    template_name = 'app/app_files/contacts/base.html'
    data["included_template"] = 'app/app_files/contacts/add_contacts.html'
    
    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/contacts.js']

    # Set link as active in menubar
    data["active_link"] = 'Contacts'
    data["breadcrumb_title"] = 'CONTACTS'

    # Initialize Forms
    data["contact_form"] = ContactsForm()
    data["tax_form"] = TaxForm()
    data["other_details_form"] = OtherDetailsForm()
    data["social_form"] = ContactsExtraForm()

    #
    # FORMSETS    
    data["address_formset"] = AddressFormset
    data["accounts_formset"] = AccountsFormset

    #
    # POST REQUEST - FORM SUBMISSION
    #
    if request.POST:
        contact_form = ContactsForm(request.POST)
        tax_form = TaxForm(request.POST)   

        ins = None

        if contact_form.is_valid():
            ins = contact_form_ins = contact_form.save(commit = False)
            contact_form_ins.user = request.user

            if contact_form_ins.is_imported_user:
                try:
                    profile = users_model.Profile.objects.get(app_id__iexact = contact_form_ins.app_id)
                    imp_user = User.objects.get(pk = profile.user_id)
                except:
                    return redirect('/unauthorized/', permanent = False)
                
                contact_form_ins.imported_user = imp_user
            
            #
            # Social form -- save
            #

            social_form = ContactsExtraForm(request.POST, request.FILES, instance = contact_form_ins)
            if social_form.is_valid():
                social_form.save()

            contact_form_ins.save() 

        #
        #
        if ins is not None:

            #
            # tax form/ other details form -- save
            #
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
            # Address Formset -- save
            #
            address_formset = AddressFormset(request.POST)
            if address_formset.is_valid():

                rownum = 0

                for form in address_formset:
                    if form.is_valid():
                        if form.data["user_address_details_set-"+str(rownum)+"-flat_no"]:
                            obj = form.save(commit = False)
                            obj.is_user = False
                            obj.contact = ins
                            obj.save()
                        rownum +=1
            
            #
            # Accounts Formset -- save
            #
            accounts_formset = AccountsFormset(request.POST)
            if accounts_formset.is_valid():

                rownum = 0

                for form in accounts_formset:
                    if form.is_valid():
                        if form.data["form-"+str(rownum)+"-account_holder_name"]:
                            obj = form.save(commit = False)
                            obj.is_user = False
                            obj.contact = ins
                            obj.save()
                        rownum +=1

        return redirect('/contacts/', data)
    return render(request, template_name, data)


#=====================================================================================
#   EDIT CONTACTS
#=====================================================================================
#

def edit_contact(request, ins = None):
        
        # Initialize 
        data = defaultdict()

        # Template 
        template_name = 'app/app_files/contacts/base.html'
        data["included_template"] = 'app/app_files/contacts/edit_contact.html'
        
        # Custom CSS/JS Files For Inclusion into template
        data["css_files"] = []
        data["js_files"] = ['custom_files/js/contacts.js']

        # Set link as active in menubar
        data["active_link"] = 'Contacts'
        data["breadcrumb_title"] = 'CONTACTS'

        if ins is not None:

            contact = None
            tax_form = None
            accounts = None

            #
            # Contact Details
            try:
                contact = contacts_model.Contacts.objects.get(pk = int(ins))
            except:
                return redirect('/unauthorized/', permanent=False)

            data["contact_details"] = contact

            data["contact_form"] = ContactsForm(instance = contact)
            data["social_form"] = ContactsExtraForm(instance = contact)

            #

            data["contact_ins"] = contact.id
            data["tax_ins"] = ""
            
            #
            # Tax Details
            try:
                tax_form = users_model.User_Tax_Details.objects.get(is_user = False, contact = contact) 
            except:
                pass

            data["tax_form_details"] = tax_form
            data["tax_form"] = TaxForm(instance = tax_form)
            data["other_details_form"] = OtherDetailsForm(instance = tax_form)

            #
            # Addresses
            contact_address_form = users_model.User_Address_Details.objects.filter(contact = contact, is_user = False)
            c_count = len(contact_address_form)

            data["contact_addresses"] = contact_address_form
            
            data["c_count"] = [i for i in range(c_count)]
            
            data["contact_address_form"] = []
            for i in range(c_count):
                data["contact_address_form"].append(EditAddressForm(instance = contact_address_form[i], prefix = 'form_{}'.format(contact_address_form[i].id)))


            data["new_address_form"] = EditAddressForm()
            data["new_accounts_form"] = AccountDetailsForm()

            #
            # Accounts
            contact_accounts_form = users_model.User_Account_Details.objects.filter(contact = contact, is_user = False)
            a_c_count = len(contact_accounts_form)

            data["contact_accounts"] = contact_accounts_form

            data["a_c_count"] = [i for i in range(a_c_count)]

            data["contact_accounts_form"] = []
            for i in range(a_c_count):
                data["contact_accounts_form"].append(AccountDetailsForm(instance = contact_accounts_form[i], prefix = 'form_{}'.format(contact_accounts_form[i].id)))

        else:    
            return redirect('/unauthorized/', permanent = False)
        return render(request, template_name, data)

#=======================================================================================
#   ADD ADDRESS DETAILS FORM
#=======================================================================================
#
def add_address_details_form(request):

    if request.POST:

        try:
            contact_ins = contacts_model.Contacts.objects.get(pk = int(request.POST["ids"]))
        except:
            return redirect('/unauthorized/', permanent = False)

        address_form = EditAddressForm(request.POST)

        if address_form.is_valid():
            ins = address_form.save(commit = False)
            ins.contact = contact_ins
            ins.is_user = False
            ins.save()

    return redirect('/contacts/edit/{}/'.format(request.POST["ids"]), permanent = False)


#=======================================================================================
#   ADD ACCOUNTS DETAILS
#=======================================================================================
#
def add_accounts_details_form(request):

    if request.POST:

        try:
            contact_ins = contacts_model.Contacts.objects.get(pk = int(request.POST["ids"]))
        except:
            return redirect('/unauthorized/', permanent = False)

        accounts_form = AccountDetailsForm(request.POST)

        if accounts_form.is_valid():
            ins = accounts_form.save(commit = False)
            ins.contact = contact_ins
            ins.is_user = False
            ins.save()

    return redirect('/contacts/edit/{}/'.format(request.POST["ids"]), permanent = False)

#=======================================================================================
#   EDIT CONTACT DETAILS
#=======================================================================================
#
def edit_contact_details_form(request):

    if request.POST:

        try:
            contact_ins = contacts_model.Contacts.objects.get(pk = int(request.POST["ids"]))
        except:
            return redirect('/unauthorized/', permanent = False)

        contact_form = ContactsForm(request.POST, instance=contact_ins)
        if contact_form.is_valid():    
            contact_form.save() 
    return redirect('/contacts/edit/{}/'.format(request.POST["ids"]), permanent = False)

#=======================================================================================
#   EDIT TAX & OTHER DETAILS
#=======================================================================================
#
def edit_tax_details_form(request):
    if request.POST:
        try:
            obj_ins = users_model.User_Tax_Details.objects.get(pk = int(request.POST["obj_ins"]))   
            tax_form = TaxForm(request.POST, instance = obj_ins)

            if tax_form.is_valid():
                tax_form.save()  
        except:
            try:
                contact_ins = contacts_model.Contacts.objects.get(pk = int(request.POST["ids"]))
            except:
                return redirect('/unauthorized/', permanent=False)

            tax_form = TaxForm(request.POST)

            if tax_form.is_valid():
                tax_form.save(commit  = False)
                tax_form.contact = contact_ins
                tax_form.save()  

    return redirect('/contacts/edit/{}/'.format(request.POST["ids"]), permanent = False)


def edit_other_details_form(request):
    if request.POST:
        try:
            obj_ins = users_model.User_Tax_Details.objects.get(pk = int(request.POST["obj_ins"]))   
            tax_form = OtherDetailsForm(request.POST, instance = obj_ins)

            if tax_form.is_valid():
                tax_form.save()  
        except:
            try:
                contact_ins = contacts_model.Contacts.objects.get(pk = int(request.POST["ids"]))
            except:
                return redirect('/unauthorized/', permanent=False)

            tax_form = OtherDetailsForm(request.POST)

            if tax_form.is_valid():
                tax_form.save(commit  = False)
                tax_form.contact = contact_ins
                tax_form.save()         
    return redirect('/contacts/edit/{}/'.format(request.POST["ids"]), permanent = False)


#=======================================================================================
#   EDIT ADDRESS DETAILS
#=======================================================================================
#
def edit_address_details_form(request):
    if request.POST:

        keys = [i for i in request.POST.keys() if "contact_person" in i]

        prefix = keys[0].replace("-contact_person", "").replace("form_", "")

        try:
            obj = users_model.User_Address_Details.objects.get(pk = int(prefix))
            address_form = EditAddressForm(request.POST, prefix='form_'+prefix, instance = obj)
            if address_form.is_valid():
                address_form.save()
        except:
            try:
                contact = Contacts.objects.get(pk = int(request.POST["ids"]))
            except:
                return redirect('/unauthorized/', permanent=False)

            address_form = EditAddressForm(request.POST, prefix='form_'+prefix)
            if address_form.is_valid():
                obj_add = address_form.save()
                obj_add.contact = contact
                obj_add.save() 
        
        return redirect('/contacts/edit/{}/'.format(request.POST["ids"]), permanent = False)

#=======================================================================================
#   EDIT ACCOUNTS DETAILS
#=======================================================================================
#
def edit_accounts_details_form(request):
    if request.POST:

        keys = [i for i in request.POST.keys() if "account_number" in i]

        prefix = keys[0].replace("-account_number", "").replace("form_", "")

        try:
            account = users_model.User_Account_Details.objects.get(pk = int(prefix))
        except:
            return redirect('/unauthorized/', permanent=False)

        account_form = AccountDetailsForm(request.POST, prefix='form_'+prefix, instance = account)
        if account_form.is_valid():
            account_form.save()

    return redirect('/contacts/edit/{}/'.format(request.POST["ids"]), permanent = False)

#=======================================================================================
#   EDIT SOCIAL DETAILS
#=======================================================================================
#
def edit_social_details_form(request):
    if request.POST:
        try:
            contact = Contacts.objects.get(pk = int(request.POST["ids"]))
        except:
            return redirect('/unauthorized/', permanent=False)
        
        social_form = ContactsExtraForm(request.POST, request.FILES, instance = contact)
        if social_form.is_valid():
            social_form.save()

    return redirect('/contacts/edit/{}/'.format(request.POST["ids"]), permanent = False)    

#================================================================================
# CHECK APPLICATION ID
# GET USER ID BASED ON THE CHECK
#================================================================================

def get_app_user_id(app_id):
    data = {'ret':0, 'id':None}
    try:
        pro = Profile.objects.get(app_id__iexact = app_id)
        data["ret"] = 1
        data["id"] = pro.user_id
    except:
        pass
    return data

#================================================================================
# CHECK APPLICATION ID
#================================================================================

def count_user_in_contact_list(user_id, imp_user_id):
    return Contacts.objects.filter(user = user_id, imported_user_id = int(imp_user_id)).count()

#================================================================================
# USER - CONTACT ALREADY PRESENT IN THE CONTACT LIST
#================================================================================

def check_app_id(request):
    data = {}
    if request.is_ajax():
        if request.POST: 
            data = get_app_user_id(request.POST["id"])
    return HttpResponse(json.dumps(data))


#================================================================================
# CHECK APPLICATION ID EXISTS IN THE CONTACT LIST
#================================================================================

def user_exists_in_list(request):
    if request.is_ajax():
        if request.POST:
            total = count_user_in_contact_list(request.user, request.POST["id"])
            return HttpResponse(total)    
        return HttpResponse(-1)
    return HttpResponse(-1)

#================================================================================
# CONTACTS FILE UPLOAD VIEW
#================================================================================

class ContactsFileUploadView(View):
    
    # Template 
    template_name = 'app/app_files/contacts/base.html'
    
    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["contacts"] = {}
    data["active_link"] = 'Contacts'
    data["breadcrumb_title"] = 'CONTACTS'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    data["included_template"] = 'app/app_files/contacts/upload_contacts.html'
    
    data["error_now"] = []
    data["row_count"] = 0

    # Documentation Import
    data["documentation_dict"] = documentation_dict.CSV_IMPORT_DICT

    #
    #
    def get(self, request):        
        self.data["error"] = ""
        self.data["upload_form"] = UploadContactsForm()
        return render(request, self.template_name, self.data)

    def post(self, request):
        self.data["upload_form"] = UploadContactsForm(request.POST, request.FILES)

        if self.data["upload_form"].is_valid():

            if str(request.FILES['csv_file']).lower().endswith('.csv'):

                self.data["upload_form"].save(commit = False)
                self.data["upload_form"].user = request.user
                obj = self.data["upload_form"].save()

                #***************************************************************
                #   Write data to database
                #***************************************************************

                file_path = settings.MEDIA_ROOT+"/"+str(obj.csv_file)
                err, self.data["row_count"] = csv_2_contacts(request.user,file_path)

                self.data["error"] = '<br>'.join(err)
            else:
                self.data["error"] = "Only CSV file is supported"
        return render(request, self.template_name, self.data)

#==============================================================================
# Function to insert contact import csv data into database
#==============================================================================
#
def csv_2_contacts(user, file_path):
    row_count = 0
    error_row = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        records = csv.DictReader(csvfile)

        fields = records.fieldnames

        contact_ins = None

        for row in records:

            #*************************************************************** 
            # Get and Set Missing/Existence of fields
            #***************************************************************
            salutation = row["salutation"] if "salutation" in fields else None
            customer_type = row["customer_type"] if "customer_type" in fields else None
            is_sub_customer = row["is_sub_customer"] if "is_sub_customer" in fields else 1
            contact_name = row["contact_name"] if "contact_name" in fields else None
            display_name = row["display_name"] if "display_name" in fields else None
            organization_type = row["organisation_type"] if "organisation_type" in fields else 1
            organization_name = row["organisation_name"] if "organisation_name" in fields else None
            
            if "is_msme_reg" in fields:
                is_msme_reg = True if row["is_msme_reg"] == 'TRUE' else False
            else:
                is_msme_reg = False

            email = row["email"] if "email" in fields else None
            phone = row["phone"] if "phone" in fields else None
            website = row["website"] if "website" in fields else None
            facebook = row["facebook"] if "facebook" in fields else None
            twitter = row["twitter"] if "twitter" in fields else None
            notes = row["notes"] if "notes" in fields else None

            contact_person = row["contact_person"] if "contact_person" in fields else None
            flat_no = row["flat_door_no"] if "flat_door_no" in fields else None
            street = row["street"] if "street" in fields else None
            city = row["city"] if "city" in fields else None
            pincode = row["pincode"] if "pincode" in fields else None
            state = row["state"] if "state" in fields else None
            country = row["country"] if "country" in fields else None

            account_number = row["account_number"] if "account_number" in fields else None 
            account_holder_name = row["account_holder_name"] if "account_holder_name" in fields else None 
            ifsc_code = row["ifsc_code"] if "ifsc_code" in fields else None 
            bank_name = row["bank_name"] if "bank_name" in fields else None 
            bank_branch_name = row["branch_name"] if "branch_name" in fields else None
            
            pan = row["pan"] if "pan" in fields else None
            gstin = row["gstin"] if "gstin" in fields else None
            gst_reg_type = row["gst_reg_type"] if "gst_reg_type" in fields else None
            business_reg_no = row["business_reg_no"] if "business_reg_no" in fields else None
            tax_reg_no = row["tax_reg_no"] if "tax_reg_no" in fields else None
            cst_reg_no = row["cst_reg_no"] if "cst_reg_no" in fields else None
            tds = row["tds"] if "tds" in fields else None
            preferred_currency = row["preferred_currency"] if "preferred_currency" in fields else None
            opening_balance = row["opening_balance"] if "opening_balance" in fields else None
            as_of = row["as_of"] if "as_of" in fields else None
            preferred_payment_method = row["preferred_payment_method"] if "preferred_payment_method" in fields else None
            preferred_delivery = row["preferred_delivery"] if "preferred_delivery" in fields else None
            invoice_terms = row["invoice_terms"] if "invoice_terms" in fields else None
            bills_terms = row["billing_terms"] if "billing_terms" in fields else None

            #***************************************************************
            # Validations
            #***************************************************************

            email_pattern = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

            url_pattern = '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'

            ifsc_pattern = '/^[A-Za-z]{4}[a-zA-Z0-9]{7}$/'

            gst_pattern = '/^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$/'

            pan_pattern = '/[A-Z]{5}[0-9]{4}[A-Z]{1}$/'

            phone_pattern = '/^\d{10}$/'

            number_pattern = '/^\d$/'

            # check email
            if not re.search(email_pattern, email) and email is not None:
                print(email)
                error_row.append("Error On Row {}: In-Valid Email. Row Skipped".format(row_count))    

                return error_row, row_count

            # check url
            if not re.search(url_pattern, website) and website is not None:
                error_row.append("Error On Row {}: In-Valid Website. Row Skipped".format(row_count))    

                return error_row, row_count

            if not re.search(url_pattern, facebook) and facebook is not None:
                error_row.append("Error On Row {}: In-Valid Facebook Link. Row Skipped".format(row_count))    

                return error_row, row_count

            if not re.search(url_pattern, twitter) and twitter is not None:
                error_row.append("Error On Row {}: In-Valid Twitter Link. Row Skipped".format(row_count))    

                return error_row, row_count

            # check PAN
            if not re.search(pan_pattern, pan) and pan is not None:
                error_row.append("Error On Row {}: In-Valid PAN. Row Skipped".format(row_count))    

                return error_row, row_count

            # check IFSC
            if not re.search(ifsc_pattern, ifsc_code) and ifsc_code is not None:
                error_row.append("Error On Row {}: In-Valid IFSC. Row Skipped".format(row_count))    

                return error_row, row_count

            # check GST
            if not re.search(gst_pattern, gstin) and gstin is not None:
                error_row.append("Error On Row {}: In-Valid GST. Row Skipped".format(row_count))    

                return error_row, row_count

            # check Phone
            if not re.search(phone_pattern, phone) and phone is not None:
                error_row.append("Error On Row {}: In-Valid Phone. Row Skipped".format(row_count))    

                return error_row, row_count

            # check Account Number
            if not re.search(number_pattern, account_number) and account_number is not None:
                error_row.append("Error On Row {}: In-Valid Account Number. Row Skipped".format(row_count))    

                return error_row, row_count


            #***************************************************************
            # Phase 1
            #***************************************************************

            if row["is_parent_record"] == 'TRUE':
                
                #***************************************************************
                # Initiate Create
                #***************************************************************

                contact = Contacts(
                    salutation = salutation,
                    customer_type = customer_type,
                    is_sub_customer = is_sub_customer,
                    contact_name = contact_name,
                    display_name = display_name,
                    organization_type = organization_type,
                    organization_name = organization_name,
                    is_msme_reg = is_msme_reg,
                    email = email,
                    phone = phone,
                    website = website,
                    facebook = facebook,
                    twitter = twitter,
                    user = user,
                    notes = notes,
                )
                
                #***************************************************************
                #   If @ret is TRUE and user is not present in the  
                #   contact list then add user to contact list.
                #   If user is present then overwrite the data with the 
                #   csv record data.
                #***************************************************************  
                 
                if row["app_id"].strip() !="":
                    ret = get_app_user_id(row["app_id"])

                    if ret["ret"] == 1:                        
                        if count_user_in_contact_list(user, ret["id"]) == 0:
                            contact.save()

                            contact.imported_user_id = ret["id"]
                            contact.app_id = row["app_id"]

                            if row["use_app_user_details"] == 'TRUE': 
                                contact.is_imported_user = True
                                
                            contact.save()
                            contact_ins = contact
                        else:
                            #***************************************************************
                            # Initiate Update
                            #***************************************************************

                            contact_ins = contact = Contacts.objects.get(app_id__iexact = row["app_id"], user = user)
                            contact.salutation = salutation
                            contact.customer_type = customer_type
                            contact.is_sub_customer = is_sub_customer
                            contact.contact_name = contact_name
                            contact.display_name = display_name
                            contact.organization_type = organization_type
                            contact.organization_name = organization_name
                            contact.is_msme_reg = is_msme_reg
                            contact.email = email
                            contact.phone = phone
                            contact.website = website
                            contact.facebook = facebook
                            contact.twitter = twitter
                            contact.notes = notes
                            contact.save()
                    else:
                        error_row.append("Error On Row {}: In-Valid APP ID. Row Skipped".format(row_count))    
                        contact_ins = None
                else:
                    contact.save()
                    contact_ins = contact
                row_count += 1

            #***************************************************************
            # Phase 2
            #***************************************************************

            if contact_ins is not None:
                
                #***************************************************************
                # Address Details
                #***************************************************************

                if "is_contact_address" in fields and row["is_contact_address"] == "TRUE":
                
                    is_billing_address = False
                    is_shipping_address = False

                    if "is_billing_address" in fields and row["is_billing_address"] == "True":
                        is_billing_address = True

                    if "is_shipping_address" in fields and row["is_shipping_address"] == "True":
                        is_shipping_address = True

                    contact_address = users_model.User_Address_Details(
                        is_user = False,
                        contact_person = contact_person, 
                        flat_no = flat_no,
                        street = street,
                        city = city,
                        pincode = pincode,
                        state = state,
                        country = country,
                        is_billing_address = is_billing_address,
                        is_shipping_address = is_shipping_address,
                        contact = contact_ins,
                    )
                    contact_address.save()

                #***************************************************************
                # Account Details
                #***************************************************************

                if "is_contact_account_details" in fields and row["is_contact_account_details"] == "TRUE":
                    
                    contact_account_details = users_model.User_Account_Details(
                        is_user = False,
                        contact = contact_ins,
                        account_number = account_number,
                        account_holder_name = account_holder_name,
                        ifsc_code = ifsc_code,
                        bank_name = bank_name,
                        bank_branch_name = bank_branch_name,
                    )
                    contact_account_details.save()

                #***************************************************************
                # Tax Details
                #***************************************************************
                if "is_contact_tax_details" in fields and row["is_contact_tax_details"] == "TRUE":
                    try:
                        tax_details = User_Tax_Details.objects.get(contact = contact_ins)

                        tax_details.pan = pan
                        tax_details.gstin = gstin
                        tax_details.gst_reg_type = gst_reg_type
                        tax_details.business_reg_no = business_reg_no
                        tax_details.tax_reg_no = tax_reg_no
                        tax_details.cst_reg_no = cst_reg_no
                        tax_details.preferred_currency = preferred_currency
                        tax_details.opening_balance = opening_balance
                        tax_details.as_of = as_of
                        tax_details.preferred_payment_method = preferred_payment_method
                        tax_details.preferred_delivery = preferred_delivery
                        tax_details.invoice_terms = invoice_terms
                        tax_details.bills_terms = bills_terms

                    except:
                        tax_details = User_Tax_Details(
                            is_user = False,
                            contact = contact_ins,
                            pan = pan,
                            gstin = gstin,
                            gst_reg_type = gst_reg_type,
                            business_reg_no = business_reg_no,
                            tax_reg_no = tax_reg_no,
                            cst_reg_no = cst_reg_no,
                            preferred_currency = preferred_currency,
                            opening_balance = opening_balance,
                            as_of = as_of,
                            preferred_payment_method = preferred_payment_method,
                            preferred_delivery = preferred_delivery,
                            invoice_terms = invoice_terms,
                            bills_terms = bills_terms,
                        )
                    
                    tax_details.save()

    return error_row, row_count

#===================================================================================================
# STATUS CHANGE
#===================================================================================================
#
def status_change(request, slug = None, ins = None):
    
    if slug is not None and ins is not None:
        try:
            contact = Contacts.objects.get(pk = int(ins))        
        except:
           return redirect('/unauthorized/', permanent=False)

        if slug == 'deactivate':
            contact.is_active = False
        elif slug == 'activate':
            contact.is_active = True
        else:
            return redirect('/unauthorized/', permanent=False)

        contact.save()
        return redirect('/contacts/', permanent=False)

    return redirect('/unauthorized/', permanent=False)


#===================================================================================================
# DELETE CHANGE
#===================================================================================================
#

def delete_contact(request, ins = None):
    if ins is not None:
        try:
            Contacts.objects.get(pk = int(ins)).delete()
        except:
            return redirect('/unauthorized/', permanent=False)

        return redirect('/contacts/', permanent=False)
    return redirect('/unauthorized/', permanent=False)

        
#===================================================================================================
# DELETE ADDRESS
#===================================================================================================
#

def delete_contact_address(request, ins = None):
    if ins is not None:
        try:
            users_model.User_Address_Details.objects.get(pk = int(ins)).delete()
        except:
            return HttpResponse(0)
        
        return HttpResponse(1)
    return HttpResponse(1)
        
#===================================================================================================
# DELETE ADDRESS
#===================================================================================================
#

def delete_accounts_details(request, ins = None):     
    if ins is not None:
        try:
            users_model.User_Account_Details.objects.get(pk = int(ins)).delete()
        except:
            return HttpResponse(0)
        
        return HttpResponse(1)
    return HttpResponse(1)

#===================================================================================================
# SEARCH CONTACTS
#===================================================================================================
#