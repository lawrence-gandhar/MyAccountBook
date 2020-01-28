from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import Contacts as C, Contacts_Email, Contact_Addresses, Contact_Account_Details
from app.models.users_model import *
from app.forms.contact_forms import *

from django.db import *

import json

#=====================================================================================
#   CONTACTS VIEW
#=====================================================================================
#
class Contacts(View):

    # Template 
    template_name = 'app/app_files/contacts/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["contacts"] = {}
    data["active_link"] = 'Contacts'
    data["breadcrumb_title"] = 'CONTACTS'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    #
    #
    def get(self, request):        

        view_type = request.GET.get('view',False)

        contacts = C.objects.filter(user = request.user)
        self.data["contacts"] = contacts

        if view_type:
            self.data["view"] = "grid"
        else:
            self.data["view"] = ""

        return render(request, self.template_name, self.data)


#=====================================================================================
#   ADD CONTACTS
#=====================================================================================
#
def add_contacts(request, slug = None, ins = None):

    # Initialize 
    data = defaultdict()

    # Template 
    template_name = 'app/app_files/contacts/add_contacts.html'
    data["included_template"] = 'app/app_files/contacts/add_contacts_step1.html'
    
    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/contacts.js']

    # Set link as active in menubar
    data["active_link"] = 'Contacts'

    data["slug"] = slug
    data["breadcrumbs"] = ''
    data["breadcrumbs_index"] = 0
    
    data["instance_title"] = None
    data["contact_form_instance"] = ins
    data["query_string"] = request.GET.get('section', None)

    # Initialize Forms
    data["contact_form"] = ContactsForm()
    data["contact_email_form"] = ContactsEmailForm()
    data["contact_address_form"] = ContactsAddressForm()
    data["contact_account_details_form"] = ContactAccountDetailsForm()

    #=========================================
    # Breadcrumbs List & Links
    #=========================================

    qStr = ''
    if data["query_string"] is not None and data["query_string"] == 'all':
        qStr = '?section='+data["query_string"]

    breadcrumbs_list = [
            '<li class="nav-item" style="float:left;padding:0px 10px;margin-left:20px;"><a href="/contacts/add/step1/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-user"></i> Basic Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step2/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-envelope-open"></i> Email Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step3/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-id-card"></i> Address Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step4/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-credit-card"></i> Account Details</a></li>'
        ]

    if ins is not None:
        try: 
            contact = C.objects.get(pk = data["contact_form_instance"], user = request.user)
            data["instance_title"] = contact.contact_name
        except C.DoesNotExist:
            return redirect('/unauthorized/', permanent = True)


    if data["slug"] is not None and data["contact_form_instance"] is not None:

        data["breadcrumbs_index"] = int(data["slug"].replace('step',''))

        if data["contact_form_instance"] is None:
            data["included_template"] = 'app/app_files/contacts/add_contacts_'+data["slug"]+'.html'
        else:
            
            try:
                contact = C.objects.get(pk = data["contact_form_instance"], user = request.user)
                data["instance_title"] = contact.contact_name

                if data["breadcrumbs_index"] == 1:
                    data["contact_form"] = ContactsForm(instance = contact)
                    counter = 1

                if data["breadcrumbs_index"] == 2:
                    data["contact_emails"] = Contacts_Email.objects.filter(contact = data["contact_form_instance"])
                    counter = data["contact_emails"].count()
                    
                if data["breadcrumbs_index"] == 3:
                    data["contact_addresses"] = Contact_Addresses.objects.filter(contact = data["contact_form_instance"])
                    counter = data["contact_addresses"].count()
                    
                if data["breadcrumbs_index"] == 4:                    
                    data["contact_account_details"] = Contact_Account_Details.objects.filter(contact = data["contact_form_instance"])
                    counter = data["contact_account_details"].count()

                if counter == 0 :
                    data["included_template"] = 'app/app_files/contacts/add_contacts_'+data["slug"]+'.html'
                else:
                    data["included_template"] = 'app/app_files/contacts/edit_contacts_'+data["slug"]+'.html'
                
            except:
                data["included_template"] = 'app/app_files/contacts/add_contacts_'+data["slug"]+'.html'

        breadcrumbs = []
        for i in range(data["breadcrumbs_index"]):
            breadcrumbs.append(breadcrumbs_list[i])

        data["breadcrumbs"] = ''.join(breadcrumbs)

    #=========================================
    # Check Slug - for creation of breadcrumbs 
    #=========================================
    if data["query_string"] is not None:
        if data["query_string"] == '':
            return redirect('/unauthorized/', permanent = True)
        elif data["query_string"] == 'all':
            data["breadcrumbs"] = ''.join(breadcrumbs_list)
        else:
            return redirect('/unauthorized/', permanent = True)

    #=========================================
    # POST REQUEST
    #=========================================
    if request.POST:

        if data["slug"] is None:
            contact_form = ContactsForm(request.POST)
            if contact_form.is_valid():
                data["contact_form_instance"] = contact_form_ins = contact_form.save(commit = False)
                contact_form_ins.user = request.user
                contact_form_ins.save()

                if contact_form_ins.email is not None:
                    email_ins = Contacts_Email.objects.create(contact = contact_form_ins)
                    email_ins.email = contact_form_ins.email
                    email_ins.is_official = True
                    email_ins.save()

                if contact_form_ins.is_imported_user:
                    try:
                        profile = Profile.objects.get(app_id__iexact = contact_form_ins.app_id)
                        imp_user = User.objects.get(pk = profile.user_id)
                    except:
                        return redirect('/unauthorized/', permanent = False)
                    try:
                        contact_form_ins.imported_user = imp_user
                        contact_form_ins.contact_name = imp_user.first_name.capitalize() +" "+imp_user.last_name.capitalize() 
                        contact_form_ins.save()
                        return redirect('/contacts/', permanent=False) 
                    except IntegrityError:
                        return redirect('/contacts/add/step1/{}'.format(data["contact_form_instance"].pk), permanent=False) 
                return redirect('/contacts/add/step3/{}'.format(data["contact_form_instance"].pk), permanent=False) 
        
        try:
            c = C.objects.get(pk = data["contact_form_instance"], user = request.user)
        except C.DoesNotExist:
            return redirect('/unauthorized/', permanent = False)

        if data["breadcrumbs_index"] == 2:            
            contact_email_form = ContactsEmailForm(request.POST or None)
            if contact_email_form.is_valid():
                contact_email = contact_email_form.save(commit = False)    
                contact_email.contact = c
                contact_email.save()
                return redirect('/contacts/add/step2/{}'.format(data["contact_form_instance"]), permanent=False) 

        if data["breadcrumbs_index"] == 3:            
            contact_address_form = ContactsAddressForm(request.POST or None)
            if contact_address_form.is_valid():
                contact_address = contact_address_form.save(commit = False)    
                contact_address.contact = c
                contact_address.save()                 
                return redirect('/contacts/add/step3/{}'.format(data["contact_form_instance"]), permanent=False) 
            
        if data["breadcrumbs_index"] == 4:            
            contact_account_details_form = ContactAccountDetailsForm(request.POST or None)
            if contact_account_details_form.is_valid():
                contact_account_details = contact_account_details_form.save(commit = False)    
                contact_account_details.contact = c
                contact_account_details.save()                
                return redirect('/contacts/add/step4/{}'.format(data["contact_form_instance"]), permanent=False) 

    return render(request, template_name, data)


#=====================================================================================
#   EDIT CONTACTS
#=====================================================================================
#
def edit_contact(request, slug = None, ins = None):
    if request.POST:
        if slug is not None and ins is not None:
            try:
                contact = C.objects.get(pk = int(ins), user = request.user)
                contact_form = ContactsForm(request.POST, instance = contact)
                
                if contact_form.is_valid(): 
                    contact_form.save()    
            except C.DoesNotExists:
                return redirect('/unauthorized/', permanent=False)
    return redirect('/contacts/add/step1/{}'.format(ins), permanent=False)

#=======================================================================================
#   FETCH EDIT CONTACT EXTRA FORMS
#=======================================================================================
#
def fetch_extra_edit_forms(request):
    if request.is_ajax():
        if request.POST:
            form_type = request.POST.get('form_type', None)
            obj_ins = request.POST.get('ins', None)

            form_html = OrderedDict()

            if form_type is not None and obj_ins is not None:
                
                #=====================================================
                # Edit Email Form
                #=====================================================
                if form_type == 'edit_contact_email':
                    labels = {
                        'email' : 'Email Address',
                        'is_official' : 'Is Official Email',
                        'is_personal' : 'Is Personal Email'
                    }
                    try:
                        obj = Contacts_Email.objects.get(pk = int(obj_ins))
                        form_data = ContactsEmailForm(instance = obj) 
                    except:
                        return HttpResponse('0')

                #=====================================================
                # Edit Address Form
                #=====================================================
                if form_type == 'edit_contact_address':
                    labels = {
                        'contact_name' : 'Contact Person',
                        'flat_no' : 'Flat/Door No',
                        'street' : 'Street/Lane',
                        'city' : 'City',
                        'state' : 'State',
                        'country' : 'Country',
                        'pincode' : 'Zip Code',
                        'is_billing_address' : 'Is Billing Address',
                        'is_shipping_address' : 'Is Shipping Address',
                    }
                    try:
                        obj = Contact_Addresses.objects.get(pk = int(obj_ins))
                        form_data = ContactsAddressForm(instance = obj)
                    except:
                        return HttpResponse('0')

                #=====================================================
                # Edit Account Form
                #=====================================================
                if form_type == 'edit_contact_account_details':
                    labels = {
                        'account_number':'Account Number',
                        'account_holder_name':'Account Holder',
                        'ifsc_code':'IFSC Code',
                        'bank_name':'Bank Name',
                        'bank_branch_name':'Branch Name',
                    }

                    try:
                        obj = Contact_Account_Details.objects.get(pk = int(obj_ins))
                        form_data = ContactAccountDetailsForm(instance = obj)
                    except:
                        return HttpResponse('0')


                #=====================================================
                # Convert Form Fields to JSON
                #=====================================================                
                form_html["id"] = {
                    'label':'id', 
                    'field':'<input type="hidden" value="'+obj_ins+'" name="id">', 
                    'label_style':'display:none'
                }
                for key in form_data.fields:
                    form_html[key] = {
                        'label': labels[key], 
                        'field':str(form_data[key]).replace("\n",""),
                        'label_style':''
                    }
                return HttpResponse(json.dumps(form_html))

            return HttpResponse('0')
        return HttpResponse('0')
    return HttpResponse('0')


#=======================================================================================
#   DELETE CONTACTS
#=======================================================================================
#
def delete_contacts(request, slug = None, ins = None, obj = None):

    if slug is not None and ins is not None and obj is not None:
        try: 
            contact = C.objects.get(pk = ins, user = request.user)
        except C.DoesNotExist:
            return redirect('/unauthorized/', permanent = True)

        slug = int(slug.replace('step',''))

        #=====================================================
        # DELETE CONTACTS EMAIL
        #=====================================================
        if slug == 2:
            try:
                CE = Contacts_Email.objects.get(pk = obj, contact = contact)
                Contacts_Email.objects.get(pk = obj).delete()
                return redirect('/contacts/add/step2/{}'.format(ins), permanent=True)
            except CE.DoesNotExists:
                return redirect('/unauthorized/', permanent = True)

        #=====================================================
        # DELETE CONTACTS ADDRESS
        #=====================================================
        if slug == 3:
            try:
                CE = Contact_Addresses.objects.get(pk = obj, contact = contact)
                Contact_Addresses.objects.get(pk = obj).delete()
                return redirect('/contacts/add/step3/{}'.format(ins), permanent=True)
            except CE.DoesNotExists:
                return redirect('/unauthorized/', permanent = True)
    
        #=====================================================
        # DELETE CONTACTS ACCOUNT DETAILS
        #=====================================================
        if slug == 4:
            try:
                CE = Contact_Account_Details.objects.get(pk = obj, contact = contact)
                Contact_Account_Details.objects.get(pk = obj).delete()
                return redirect('/contacts/add/step4/{}'.format(ins), permanent=True)
            except CE.DoesNotExists:
                return redirect('/unauthorized/', permanent = True)
        
    return redirect('/unauthorized/', permanent = True)

#================================================================================
# EDIT CONTACT FORMS 
#================================================================================

def edit_contact_forms(request):
    if request.POST:
        slug = request.POST.get('slug', None)
        obj_ins = request.POST.get('id', None)
        form_ins = request.POST.get('form_ins', None)

        if slug is not None and obj_ins is not None:

            redirect_url = False

            #==========================================================
            # EDIT EMAIL
            #==========================================================
            if slug == "step2":
                obj = Contacts_Email.objects.get(pk = int(obj_ins))
                email_form = ContactsEmailForm(request.POST, instance = obj)
                
                if email_form.is_valid():
                    email_form.save()
                    redirect_url = True
            
            #==========================================================
            # EDIT ADDRESS DETAILS
            #==========================================================

            if slug == "step3":
                obj = Contact_Addresses.objects.get(pk = int(obj_ins))
                address_form = ContactsAddressForm(request.POST, instance = obj)

                if address_form.is_valid():
                    address_form.save()
                    redirect_url = True

            #==========================================================
            # EDIT ACCOUNT DETAILS
            #==========================================================

            if slug == "step4":
                obj = Contact_Account_Details.objects.get(pk = int(obj_ins))
                accounts_form = ContactAccountDetailsForm(request.POST, instance = obj)

                if accounts_form.is_valid():
                    accounts_form.save()
                    redirect_url = True

            #==========================================================
            # REDIRECTION ON SUCCESS OR FAILURE
            #==========================================================
            if redirect_url:                
                return redirect('/contacts/add/{}/{}'.format(slug, form_ins), permanent=True)
            return redirect('/unauthorized/', permanent = True)
        return redirect('/unauthorized/', permanent = True)
    return redirect('/unauthorized/', permanent = True)


#================================================================================
# CHECK APPLICATION ID
#================================================================================

def check_app_id(request):
    if request.is_ajax():
        if request.POST: 

            data = {'ret':0, 'data':None}

            try:
                pro = Profile.objects.get(app_id__iexact = request.POST["id"])
                data["ret"] = 1
                return HttpResponse(json.dumps(data))
            except:
                return HttpResponse(json.dumps(data))
        return HttpResponse(json.dumps(data))
    return HttpResponse(json.dumps(data))