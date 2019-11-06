from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Contacts(View):
    template_name = 'app/app_files/contacts/index.html'

    data["css_files"] = []
    data["js_files"] = []
    data["active_link"] = 'Contacts'

    def get(self, request):
        return render(request, self.template_name, self.data)