from django.urls import path
from .views import ProjectsListView

urlpatterns = [
    path("all/", ProjectsListView.as_view(), name="projects_list"),
]