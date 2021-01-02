from django.db import models


from tinymce.models import HTMLField


class Skills(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    image = models.ImageField(blank=False, null=False, upload_to='skills_image/')

class Education(models.Model):
    school_image = models.ImageField(blank=False, null=False, upload_to='education_image/')
    certificate = models.ImageField(blank=False, null=False, upload_to='education_image/')
    school_name = models.CharField(max_length=80)
    body = models.TextField(max_length=1500)
