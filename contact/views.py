from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import ListView

from contact.models import SocialLinks


class SocialLinksListView(ListView):
    template_name = 'contact/contact.html'
    model = SocialLinks

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')


# def contactme(request):
# #wysylanie maila
#     return render(request, 'contact/contact.html')
