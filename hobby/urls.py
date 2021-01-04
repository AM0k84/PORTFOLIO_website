from django.urls import path

from .views import HobbyListView

app_name = 'hobby'

urlpatterns = [
    path("", HobbyListView.as_view(), name="all_hobbys"),
]
