from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.invoice_model import Invoice
from app.models.collects_model import *
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
    data["included_template"] = 'app/app_files/invoice/template_design_form.html'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/design_template.js']


    def get(self, request, *args, **kwargs):
        self.data["invoice_design_form"] = InvoiceDesignerForm()
        return render(request, self.template_name, self.data)

    def post(self, request, *args, **kwargs):
        form = InvoiceDesignerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, self.data)    
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
    data["invoice__template_design_form"] = ''

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

    # Initialize Forms
    data["invoice__template_design_form"] = ''

    #
    #
    #
    def get(self, request, *args, **kwargs):

        ins = int(self.kwargs['ins'])

        try:
            collect = Collections.objects.get(pk = ins)
        except:
            return redirect('/unauthorized/', permanent = True)

        self.data["contact"] = collect.contact.contact_name
        self.data["collections"] = collect
        self.data["partial_collections"] = CollectPartial.objects.filter(collect_part = collect)

        return render(request, self.template_name, self.data)

    #
    # 
    #     