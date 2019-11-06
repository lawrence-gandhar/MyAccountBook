from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def index(request):
    template_name = 'app/registration/index.html'
    return render(request, template_name, {})


class Dashboard(View):
    template_name = 'app/app_files/index.html'

    def get(self, request):
        return render(request, self.template_name)


class Contacts(View):
    template_name = 'app/app_files/contacts/index.html'

    def get(self, request):
        return render(request, self.template_name, {})