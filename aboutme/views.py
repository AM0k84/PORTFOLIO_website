from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from aboutme.models import Skills, Education


class AboutmeListView(ListView):
    template_name = "aboutme/aboutme.html"
    model = Skills

    def get_queryset(self):
        return self.model.objects.all().order_by('pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_education'] = Education.objects.all().order_by('-pk')
        return context
