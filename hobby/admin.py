from django.contrib import admin


from hobby.models import HobbyGallery, MyHobby

class MyHobbyAdmin(admin.ModelAdmin):
    list_display = ['name']

class GalleryMyHobbyAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(HobbyGallery, GalleryMyHobbyAdmin)
admin.site.register(MyHobby, MyHobbyAdmin)
