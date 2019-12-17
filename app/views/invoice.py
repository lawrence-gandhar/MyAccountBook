from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import Contacts as C
from app.forms.contact_forms import *

import json

#=====================================================================================
#   CONTACT - CREATE INVOICE
#=====================================================================================
#
def create_invoice(request, ins = None):
    
    # Initialize 
    data = defaultdict()
    
    # Template 
    template_name = 'app/app_files/invoice/index.html'
    data["included_template"] = 'app/app_files/invoice/create_invoice.html'

    # Set link as active in menubar
    data["active_link"] = 'Invoice'


    return render(request, template_name, data)