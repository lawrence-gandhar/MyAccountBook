from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import Contacts as C
from app.models.users_model import *
from app.forms.contact_forms import *

import json

#=====================================================================================
#   CONTACTS VIEW
#=====================================================================================
#
class Collections(View):

    # Template 
    template_name = 'app/app_files/contacts/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["active_link"] = 'Collections'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    #
    #
    def get(self, request):        
        return render(request, self.template_name, self.data)
