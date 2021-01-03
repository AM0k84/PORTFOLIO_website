from django.db import models

class SocialLinks(models.Model):
    image = models.ImageField(blank=False, null=False, upload_to='social_image/')
    social_link = models.URLField(max_length=200)