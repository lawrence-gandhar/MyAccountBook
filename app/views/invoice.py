from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.invoice_model import Invoice
from app.forms.invoice_forms import *

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

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    def get(self, request):
        return render(request, self.template_name, self.data)




#=====================================================================================
#   CONTACT - CREATE INVOICE
#=====================================================================================
#
def create_invoice(request, ins = None):
    
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
    data["invoice__template_design_form"] = ''

    return render(request, template_name, data)