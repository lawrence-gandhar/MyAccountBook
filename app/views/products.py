from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.db.models import *
from app.models import *
from app.forms.items_form import * 

import json


#========================================================================================
#
#========================================================================================

def view_products(request, *args, **kwargs):
    # Template 
    template_name = 'app/app_files/products/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []
    data["active_link"] = 'Products'

    data["included_template"] = 'app/app_files/products/add_products_form.html'

    return render(request, template_name, data)    

#========================================================================================
#
#========================================================================================
class AddProducts(View):

    # Template 
    template_name = 'app/app_files/products/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []
    data["active_link"] = 'Products'

    data["included_template"] = 'app/app_files/products/add_products_form.html'

    data["add_product_form"] = ProductForm()
    data["add_product_images_form"] = ProductPhotosForm()
    #
    #
    #
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)

    def post(self, request, *args, **kwargs):
        
        add_product = ProductForm(request.POST or None)
        add_images = ProductPhotosForm(request.FILES or None)

        if add_product.is_valid():
            add_product.save(commit = False)
            add_product.user = request.user
            ins = add_product.save()

        if add_images.is_valid():
            for img in request.FILES.getlist('product_image'):
                img_save = ProductPhotos(
                    product_image = img,
                    product = ins
                )

                img_save.save()
        
        return redirect('/products/', permanent = False)
