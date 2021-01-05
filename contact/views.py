
from django.shortcuts import render

from django.core.mail import send_mail
from django.views.generic import ListView


# from contact.models import SocialLinks


# class SocialLinksListView(ListView):
#     template_name = 'contact/contact.html'
#     model = SocialLinks
#
#     def get_queryset(self):
#         return self.model.objects.all().order_by('pk')
from contact.models import SocialLinks


def contactme(request):
    social_icons = SocialLinks.objects.all()

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            f"{message_name} wysłał Ci wiadomość",  # subject
            f"Treść {message}, odpowiedz do {message_email}",  # message
            message_email,  # from_email
            ['l.chalinski@gmail.com'],  # to_email

        )

        return render(request, 'contact/contact.html', {'icons': social_icons, 'message_name': message_name})
    else:

        return render(request, 'contact/contact.html', {'icons': social_icons})
