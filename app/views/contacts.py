from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Contacts(View):
    template_name = 'app/app_files/contacts/index.html'

    def get(self, request):
        return render(request, self.template_name, {})