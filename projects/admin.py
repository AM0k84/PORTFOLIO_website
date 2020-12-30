from django.contrib import admin

from projects.models import Project, ProjectCategory


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'snippet', 'project_categories']
    prepopulated_fields = {'slug': ('title',)}


class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'tool_name', 'slug')
    prepopulated_fields = {'slug': ('tool_name',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
