from django.urls import path
from .views import ProjectsListView

app_name = 'projects'

urlpatterns = [
    path("all/", ProjectsListView.as_view(), name="all_projects"),
]