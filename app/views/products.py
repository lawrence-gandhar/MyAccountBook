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

    data["included_template"] = 'app/app_files/products/view_products.html'

    #*****************************************************************************
    # PRODUCT LISTING
    #*****************************************************************************

    products = ProductsModel.objects.prefetch_related('productphotos_set').filter(user = request.user)

    data["products"] = products

    return render(request, template_name, data)    

#========================================================================================
# ADD PRODUCT
#========================================================================================
# 
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

#========================================================================================
# ADD PRODUCT CATEGORY
#========================================================================================
#
class ProductCategoryView(View):
    
    # Template 
    template_name = 'app/app_files/products/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/tree_view.js']
    data["active_link"] = 'Products'

    data["included_template"] = 'app/app_files/products/view_product_category.html'

    data["add_product_form"] = ProductForm()
    data["add_product_images_form"] = ProductPhotosForm()
    #
    #
    #
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)
