from django.urls import path

from contact.views import SocialLinksListView

app_name = 'contact'

urlpatterns = [
    path("", SocialLinksListView.as_view(), name="contact"),

]
