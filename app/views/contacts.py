from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from collections import OrderedDict, defaultdict

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
def add_contacts(request, slug = None):
    template_name = 'app/app_files/contacts/add_contacts.html'

    data = defaultdict()
    data["active_link"] = 'Contacts'

    data["contact_form"] = ContactsForm()
    data["contact_email_form"] = ContactsEmailForm()
    data["contact_address_form"] = ContactsAddressForm()
    data["contact_account_details_form"] = ContactAccountDetailsForm()

    data["slug"] = slug



    return render(request, template_name, data)