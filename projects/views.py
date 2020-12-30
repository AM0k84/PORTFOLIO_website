from django.shortcuts import render
from django.views.generic import ListView

from projects.models import Project

app_name = 'projects'

class ProjectsListView(ListView):
    template_name = "projects/all_projects.html"
    model = Project

    def get_queryset(self):
        return self.model.objects.all()
