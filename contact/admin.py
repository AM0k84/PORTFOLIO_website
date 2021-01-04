from django.contrib import admin

from contact.models import SocialLinks


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'social_link']


admin.site.register(SocialLinks, SocialLinksAdmin)
