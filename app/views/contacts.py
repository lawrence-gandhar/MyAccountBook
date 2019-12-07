from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import Contacts as C
from app.forms.contact_forms import *

import json


class Contacts(View):
    template_name = 'app/app_files/contacts/index.html'

    data = defaultdict()

    data["css_files"] = []
    data["js_files"] = []

    data["view"] = ""
    data["contacts"] = {}

    data["active_link"] = 'Contacts'

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
def add_contacts(request, slug = None, ins = None):
    template_name = 'app/app_files/contacts/add_contacts.html'

    data = defaultdict()
    data["active_link"] = 'Contacts'
    data["css_files"] = ['']
    data["js_files"] = ['custom_files/js/contacts.js']


    data["contact_form"] = ContactsForm()
    data["contact_email_form"] = ContactsEmailForm()
    data["contact_address_form"] = ContactsAddressForm()
    data["contact_account_details_form"] = ContactAccountDetailsForm()

    data["slug"] = slug
    data["breadcrumbs"] = ''
    data["breadcrumbs_index"] = 0
    data["included_template"] = 'app/app_files/contacts/add_contacts_step1.html'
    data["add_proxy"] = None

    data["instance_title"] = None

    data["contact_form_instance"] = ins

    data["query_string"] = request.GET.get('section', None)

    breadcrumbs_list = [
            '<li class="nav-item" style="float:left;padding:0px 10px;margin-left:20px;"><a href="/contacts/add/step1/'+ str(data["contact_form_instance"]) +'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-user"></i> Basic Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step2/'+ str(data["contact_form_instance"]) +'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-envelope-open"></i> Email Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step3/'+ str(data["contact_form_instance"]) +'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-id-card"></i> Address Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step4/'+ str(data["contact_form_instance"]) +'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-credit-card"></i> Account Details</a></li>'
        ]

    if data["query_string"] is not None:
        if data["query_string"] == '':
            return redirect('/unauthorized/', permanent = True)
        elif data["query_string"] == 'all':
            data["breadcrumbs"] = ''.join(breadcrumbs_list)
        else:
            return redirect('/unauthorized/', permanent = True)
                        

    #=========================================
    # Check Slug - for creation of breadcrumbs
    #=========================================

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
    # POST REQUEST
    #=========================================
    if request.POST:

        if data["slug"] is None:
            contact_form = ContactsForm(request.POST)
            if contact_form.is_valid():
                data["contact_form_instance"] = contact_form_ins = contact_form.save(commit = False)
                contact_form_ins.user = request.user
                contact_form_ins.save()

                return redirect('/contacts/add/step2/{}'.format(data["contact_form_instance"].pk), permanent=True) 
        
        try:
            c = C.objects.get(pk = data["contact_form_instance"], user = request.user)
        except C.DoesNotExist:
            return redirect('/unauthorized/', permanent = True)

        if data["breadcrumbs_index"] == 2:            
            contact_email_form = ContactsEmailForm(request.POST or None)
            if contact_email_form.is_valid():
                contact_email = contact_email_form.save(commit = False)    
                contact_email.contact = c
                contact_email.save()

                data["add_another"] = request.POST.get('add_another', None)

                if data["add_another"] == '1':
                    return redirect('/contacts/add/step2/{}'.format(data["contact_form_instance"]), permanent=True) 
                return redirect('/contacts/add/step3/{}'.format(data["contact_form_instance"]), permanent=True) 

        if data["breadcrumbs_index"] == 3:            
            contact_address_form = ContactsAddressForm(request.POST or None)
            if contact_address_form.is_valid():
                contact_address = contact_address_form.save(commit = False)    
                contact_address.contact = c
                contact_address.save()

                data["add_another"] = request.POST.get('add_another', None)

                if data["add_another"] == '1':
                    return redirect('/contacts/add/step3/{}'.format(data["contact_form_instance"]), permanent=True) 
                return redirect('/contacts/add/step4/{}'.format(data["contact_form_instance"]), permanent=True) 
            
        if data["breadcrumbs_index"] == 4:            
            contact_account_details_form = ContactAccountDetailsForm(request.POST or None)
            if contact_account_details_form.is_valid():
                contact_account_details = contact_account_details_form.save(commit = False)    
                contact_account_details.contact = c
                contact_account_details.save()

                return redirect('/contacts/add/step4/{}'.format(data["contact_form_instance"]), permanent=True) 

        return render(request, template_name, data) 
    return render(request, template_name, data)


#=====================================================================================
#   EDIT CONTACTS
#=====================================================================================

def edit_contact(request, slug = None, ins = None):
    if request.POST:
        if slug is not None and ins is not None:

            try:
                contact = C.objects.get(pk = int(ins), user = request.user)
                
                contact_form = ContactsForm(request.POST, instance = contact)
                contact_form.save()
            except C.DoesNotExists:
                return redirect('/unauthorized/', permanent=True)
    return redirect('/contacts/add/step1/{}'.format(ins), permanent=True)

#=======================================================================================
#   FETCH EDIT CONTACT EXTRA FORMS
#=======================================================================================

def fetch_extra_edit_forms(request):
    if request.is_ajax():
        if request.POST:
            form_type = request.POST.get('form_type', None)
            obj_ins = request.POST.get('ins', None)

            form_html = OrderedDict()

            if form_type is not None and obj_ins is not None:
                pass

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

                for key in form_data.fields:
                    form_html[key] = {'label': labels[key], 'field':str(form_data[key]).replace("\n","")}
                return HttpResponse(json.dumps(form_html))

            return HttpResponse('0')
        return HttpResponse('0')
    return HttpResponse('0')


#
#
#
def delete_contacts(request, slug = None, ins = None, obj = None):

    if slug is not None and ins is not None and obj is not None:
        try: 
            contact = C.objects.get(pk = ins, user = request.user)
        except C.DoesNotExist:
            return redirect('/unauthorized/', permanent = True)

        slug = int(slug.replace('step',''))

        if slug == 2:
            try:
                CE = Contacts_Email.objects.get(pk = obj, contact = contact)
                Contacts_Email.objects.get(pk = obj).delete()
                return redirect('/contacts/add/step2/{}'.format(ins), permanent=True)
            except CE.DoesNotExists:
                return redirect('/unauthorized/', permanent = True)
        
    return redirect('/unauthorized/', permanent = True)