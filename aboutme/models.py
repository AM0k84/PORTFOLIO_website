from django.db import models


from tinymce.models import HTMLField


class Skills(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    image = models.ImageField(blank=False, null=False, upload_to='skills_image/')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Skills'


class Education(models.Model):
    school_image = models.ImageField(blank=False, null=False, upload_to='education_image/')
    certificate = models.ImageField(blank=False, null=False, upload_to='education_image/')
    school_name = models.CharField(max_length=80)
    body = models.TextField(max_length=1500)
    date_from = models.PositiveSmallIntegerField()
    date_to = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.school_name}"

    class Meta:
        verbose_name_plural = 'Education'

