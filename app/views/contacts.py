from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import Contacts as C
from app.forms.contact_forms import *


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

        contacts = C.objects.all()
        self.data["contacts"] = contacts

        if view_type:
            self.data["view"] = "grid"
        else:
            self.data["view"] = ""

        return render(request, self.template_name, self.data)


#
#   ADD CONTACTS
#
def add_contacts(request, slug = None, ins = None):
    template_name = [
        'app/app_files/contacts/add_contacts.html',
        'app/app_files/contacts/add_contacts.html',
        'app/app_files/contacts/add_contacts.html',
        'app/app_files/contacts/add_contacts.html',
    ]

    data = defaultdict()
    data["active_link"] = 'Contacts'

    data["contact_form"] = ContactsForm()
    data["contact_email_form"] = ContactsEmailForm()
    data["contact_address_form"] = ContactsAddressForm()
    data["contact_account_details_form"] = ContactAccountDetailsForm()

    data["slug"] = slug
    data["breadcrumbs"] = ''

    data["contact_form_instance"] = ins

    #=========================================
    # Check Slug - for creation of breadcrumbs
    # 
    #=========================================

    if data["slug"] is not None and data["contact_form_instance"] is not None:

        breadcrumbs_list = [
            '<li class="nav-item" style="float:left;padding:0px 10px;margin-left:20px;"><a href="/contacts/add/step1/'+ str(data["contact_form_instance"]) +'" style="color:#FFFFFF; text-decoration:none;"><i class="fas fw fa-user"></i> Basic Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step2/'+ str(data["contact_form_instance"]) +' %}" style="color:#FFFFFF; text-decoration:none;" title="View Contacts As List"><i class="fas fw fa-envelope-open"></i> Email Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step3/'+ str(data["contact_form_instance"]) +' %}" style="color:#FFFFFF; text-decoration:none;" title="View Contacts As Grid"><i class="fas fw fa-id-card"></i> Address Details</a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step4/'+ str(data["contact_form_instance"]) +' %}" style="color:#FFFFFF; text-decoration:none;" title="View Contacts As Grid"><i class="fas fw fa-credit-card"></i> Account Details</a></li>'
        ]

        breadcrumbs_index = int(data["slug"].replace('step',''))

        breadcrumbs = []
        for i in range(breadcrumbs_index):
            breadcrumbs.append(breadcrumbs_list[i])

        data["breadcrumbs"] = ''.join(breadcrumbs)

    if request.POST:

        contact_form = ContactsForm(request.POST)
        if contact_form.is_valid():
             messages.success(request, 'The form is valid.')
             data["contact_form_instance"] = contact_form.save()
             return redirect('/contacts/add/step2/{}'.format(data["contact_form_instance"].pk), permanent=True) 
        else:
            messages.error(request, 'The form is invalid.')
            return render(request, template_name, data)
        


    return render(request, template_name, data)