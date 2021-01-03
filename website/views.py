from django.shortcuts import render
from django.views import View

from aboutme.models import Skills


class Home(View):
    template_name = "website/home.html"

    def get(self, request):
        return render(request, self.template_name, {})

