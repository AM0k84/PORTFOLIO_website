from django.db import models


from tinymce.models import HTMLField


class Skills(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    image = models.ImageField(blank=False, null=False, upload_to='skills_image/')