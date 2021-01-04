from django.contrib import admin


from aboutme.models import Skills, Education

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['title']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['school_name']



admin.site.register(Skills, SkillsAdmin)
admin.site.register(Education, EducationAdmin)