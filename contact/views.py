
from django.views.generic import ListView


from contact.models import SocialLinks




class SocialLinksListView(ListView):
    template_name = 'contact/contact.html'
    model = SocialLinks

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')
