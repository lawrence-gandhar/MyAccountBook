from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from django.conf import settings

from app.models.invoice_model import *
from app.models.collects_model import *
from app.models.items_model import *
from app.models.users_model import *
from app.models.contacts_model import *

from app.other_constants import country_list

import json


#
# FETCH CONTACT BILLING/SHIPPING ADDRESSES 
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
