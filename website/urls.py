from django.urls import path
from website.views import Home

app_name = 'website'

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
