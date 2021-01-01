
from django.views.generic import ListView

from hobby.models import MyHobby


class HobbyListView(ListView):
    template_name = "hobby/hobby_list.html"
    model = MyHobby

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')
