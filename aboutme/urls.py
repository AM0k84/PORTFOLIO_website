from django.urls import path

from .views import AboutmeListView

app_name = 'aboutme'

urlpatterns = [
    path("", AboutmeListView.as_view(), name="aboutme"),

]
