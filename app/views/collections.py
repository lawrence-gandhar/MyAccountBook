from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import *
from app.models.users_model import *
from app.models.collects_model import Collections as Collect
from app.forms.collection_forms import *

import json

#=====================================================================================
#   CONTACTS VIEW
#=====================================================================================
#
def view_collections(request):

    # Template 
    template_name = 'app/app_files/collections/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["active_link"] = 'Collections'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    data["included_template"] = 'app/app_files/collections/view_collections.html'
 
    data["collections"] = Collect.objects.filter(user = request.user)  
    return render(request, template_name, data)

#=====================================================================================
#   VIEW CONTACT COLLECTIONS
#=====================================================================================
#
def view_contact_collections(request, *args, **kwargs):
    # Template 
    template_name = 'app/app_files/collections/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["active_link"] = 'Collections'

    data["included_template"] = 'app/app_files/collections/view_collections.html'

    try:
        contact = Contacts.objects.get(pk = int(kwargs["ins"]))
    except:
        return redirect('/unauthorized/', permanent = True)

    data["collections"] = Collect.objects.filter(user = request.user) 
    data["collections"] = data["collections"].filter(contact = contact)
    return render(request, template_name, data)


#=====================================================================================
#   ADD COLLECTION
#=====================================================================================
#
class AddCollections(View):

    # Template 
    template_name = 'app/app_files/collections/index.html'

    data = defaultdict()

    data["included_template"] = 'app/app_files/collections/add_collections.html'

    data["css_files"] = ['all_page/plugins/bootstrap-datepicker/bootstrap-datepicker.min.css']
    data["js_files"] = ['all_page/plugins/bootstrap-datepicker/bootstrap-datepicker.min.js', 'custom_files/js/collections.js']

    data["active_link"] = 'Collections'
    
    #
    #
    def get(self, request):
        self.data["collection_form"] = CollectionsForm(request.user)
        return render(request, self.template_name, self.data)
    
    #
    #
    def post(self, request):
        collection_form = CollectionsForm(request.user, request.POST or None)
        
        if collection_form.is_valid():
            try:
                contact = Contacts.objects.get(pk = int(request.POST["contact"]))
            except:
                return redirect('/unauthorized/', permanent = True)

            obj = collection_form.save()
            obj.contact = contact         
            obj.user = request.user
            obj.save()
            return redirect('/collections/', permanent=True) 
        return render(request, self.template_name, self.data)

#=====================================================================================
#   ADD COLLECTION IN PARTS
#=====================================================================================
#
class AddPartialCollection(View):

    # Template 
    template_name = 'app/app_files/collections/index.html'

    data = defaultdict()

    data["included_template"] = 'app/app_files/collections/add_collections_partial.html'

    data["css_files"] = ['all_page/plugins/bootstrap-datepicker/bootstrap-datepicker.min.css']
    data["js_files"] = ['all_page/plugins/bootstrap-datepicker/bootstrap-datepicker.min.js', 'custom_files/js/collections.js']

    data["active_link"] = 'Collections'

    data["ins"] = None

    #
    #
    #
    def get(self, request, *args, **kwargs):
        
        ins = int(self.kwargs["ins"])

        try:
            collect = Collect.objects.get(pk = ins, collection_status__lt = 3)
        except:
            return redirect('/unauthorized/', permanent = True)

        self.data["collections"] = Collect.objects.filter(pk = ins)
        self.data["partial_collections"] = CollectPartial.objects.filter(collect_part = collect)

        self.data["collection_form"] = CollectPartialForm()
        return render(request, self.template_name, self.data)

    #
    #
    #
    def post(self, request, *args, **kwargs):
        ins = int(self.kwargs["ins"])

        collect = Collect.objects.get(pk = ins, user = request.user)
        
        collection_form = CollectPartialForm(request.POST or None)

        if collection_form.is_valid():            
            obj = collection_form.save()
            obj.collect_part = collect  
            obj.user = request.user
            obj.save()
            return redirect('/collections/', permanent=True) 
        return render(request, self.template_name, self.data)