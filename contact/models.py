from django.db import models

class SocialLinks(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=False, null=False, upload_to='social_image/')
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Social Links'
