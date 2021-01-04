from django.db import models
from tinymce.models import HTMLField
from embed_video.fields import EmbedVideoField


class HobbyGallery(models.Model):
    name = models.CharField(max_length=50)
    image1 = models.ImageField(blank=False, null=False, upload_to='hobby_image/')
    image2 = models.ImageField(blank=False, null=False, upload_to='hobby_image/')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Gallerys'


class MyHobby(models.Model):
    galery = models.OneToOneField(HobbyGallery, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = HTMLField(max_length=1250)
    youtube_video1 = EmbedVideoField(null=True, blank=True)
    youtube_video2 = EmbedVideoField(null=True, blank=True)
    youtube_video3 = EmbedVideoField(null=True, blank=True)
    iframe = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Hobbys'



