from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from collections import OrderedDict, defaultdict


class Contacts(View):
    template_name = 'app/app_files/contacts/index.html'

    data = defaultdict()

    data["css_files"] = []
    data["js_files"] = []

    data["view"] = ""

    data["active_link"] = 'Contacts'

    def get(self, request):        

        view_type = request.GET.get('view',False)

        if view_type:
            self.data["view"] = "grid"
        else:
            self.data["view"] = ""


        return render(request, self.template_name, self.data)