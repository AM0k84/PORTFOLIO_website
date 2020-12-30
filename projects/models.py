from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


class ProjectCategory(models.Model):
    tool_name = models.CharField(max_length=128)
    slug = models.SlugField(null=False, unique=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tool_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.tool_name

    class Meta:
        verbose_name_plural = 'Project categories'


class Project(models.Model):
    title = models.CharField(max_length=120)
    category = models.ManyToManyField(ProjectCategory, related_name='projects')
    snippet = models.TextField(max_length=500, null=False)
    body = HTMLField(max_length=1500, null=False)
    github_repository = models.URLField(max_length=200)
    image = models.ImageField(blank=False, null=False, upload_to='project_image/')
    image2 = models.ImageField(blank=False, null=False, upload_to='project_image/')
    image3 = models.ImageField(blank=False, null=False, upload_to='project_image/')
    slug = models.SlugField(null=False, unique=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'
