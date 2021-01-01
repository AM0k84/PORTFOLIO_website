from django.db import models


class MyHobby(models.Model):
    name = models.CharField(max_length=80)
