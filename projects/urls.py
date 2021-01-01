from django.urls import path

from .views import ProjectsListView, CategoryProjectListView, ProjectDetailView

app_name = 'projects'

urlpatterns = [
    path("", ProjectsListView.as_view(), name="all_projects"),
    path('category/<slug:slug>/', CategoryProjectListView.as_view(), name='category_projects_list'),
    path('<int:pk>/<slug:slug>', ProjectDetailView.as_view(), name='project_detail'),
]

