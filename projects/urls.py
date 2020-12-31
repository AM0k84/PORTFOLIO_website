from django.urls import path

from .views import ProjectsListView, CategoryProjectListView

app_name = 'projects'

urlpatterns = [
    path("", ProjectsListView.as_view(), name="all_projects"),
    path('category/<slug:slug>/', CategoryProjectListView.as_view(), name='category_projects_list'),
]

