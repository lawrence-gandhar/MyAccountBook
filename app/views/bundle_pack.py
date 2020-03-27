from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.db.models import *
from app.models import *
from app.forms import * 

import json

#
#
#
class ProductBundelView(View):

    # Template 
    template_name = 'app/app_files/product_bundle/index.html'

    # Initialize 
    data = defaultdict()

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []
    data["active_link"] = 'Products'
    data["breadcrumb_title"] = 'PRODUCTS'

    data["included_template"] =  'app/app_files/product_bundle/view_product_bundles.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)

    def post(self, request, *args, **kwargs):
        return HttpResponse()


