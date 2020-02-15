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

    inventory = StockModel.objects.filter(user = request.user)
    data["products"] = inventory

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

    data["included_template"] = 'app/app_files/inventory/view_inventory.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)