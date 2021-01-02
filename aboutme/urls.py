from django.urls import path

from .views import SkillsListView

app_name = 'aboutme'

urlpatterns = [
    path("", SkillsListView.as_view(), name="aboutme"),

]
