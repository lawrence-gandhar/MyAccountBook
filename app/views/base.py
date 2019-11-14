from django.views import View
from django.shortcuts import render


class UnAuthorized(View):

    def get(self, request):
        template_name = 'app/base/error_page.html'
        return render(request, template_name, {})