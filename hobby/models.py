from django.db import models
from tinymce.models import HTMLField


class HobbyGallery(models.Model):
    image1 = models.ImageField(blank=False, null=False, upload_to='hobby_image/')
    image2 = models.ImageField(blank=False, null=False, upload_to='hobby_image/')
    image3 = models.ImageField(blank=False, null=False, upload_to='hobby_image/')
    image4 = models.ImageField(blank=False, null=False, upload_to='hobby_image/')


class MyHobby(models.Model):
    galery = models.OneToOneField(HobbyGallery, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = HTMLField(max_length=1250)
    iframe = models.CharField(max_length=1000)


