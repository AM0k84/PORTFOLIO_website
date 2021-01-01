from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from projects.models import Project, ProjectCategory

app_name = 'projects'


class ProjectsListView(ListView):
    template_name = "projects/all_projects.html"
    model = Project

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')


class CategoryProjectListView(ListView):
    template_name = "projects/project_category.html"
    queryset = Project.objects.order_by('-pk')

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            category__slug=self.kwargs['slug'])

    def projectcategory(self):
        return get_object_or_404(ProjectCategory, slug=self.kwargs['slug'])


class ProjectDetailView(DetailView):
    template_name = "projects/project_detail.html"
    model = Project