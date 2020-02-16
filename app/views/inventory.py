from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.db.models import *
from app.models import *
from app.forms.items_form import * 

import json


#========================================================================================
#   VIEW/LIST STOCK DETAILS
#========================================================================================
#
def view_inventory(request, *args, **kwargs):
    # Template 
    template_name = 'app/app_files/inventory/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []
    data["active_link"] = 'Inventory'
    data["breadcrumb_title"] = 'INVENTORY'

    data["included_template"] = 'app/app_files/inventory/view_inventory.html'

    #*****************************************************************************
    # PRODUCT LISTING
    #*****************************************************************************

    inventory = Inventory.objects.filter(user = request.user)
    data["inventory"] = inventory

    return render(request, template_name, data)    


#========================================================================================
#   ADD INVENTORY
#========================================================================================
#
class AddInventory(View):
    # Template 
    template_name = 'app/app_files/inventory/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []
    data["active_link"] = 'Inventory'
    data["breadcrumb_title"] = 'INVENTORY'

    data["included_template"] = 'app/app_files/inventory/add_inventory_form.html'

    data["inventory_form"] = InventoryForm() 

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)

    def post(self, request, *args, **kwargs):

        inventory_form = InventoryForm(request.POST)

        if inventory_form.is_valid():
            ins = inventory_form.save()
            ins.user = request.user
            ins.save()

            return redirect('/inventory/', permanent = False)
        return redirect('/inventory/add/', permanent = False)
        
#========================================================================================
#   INVENTORY PRODUCTS
#========================================================================================
#

class InventoryProducts(View):

    # Template 
    template_name = 'app/app_files/inventory/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []
    data["active_link"] = 'Inventory'
    data["breadcrumb_title"] = 'INVENTORY'

    data["included_template"] = 'app/app_files/inventory/view_inventory_products.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)