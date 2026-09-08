from django.db import models

from ckeditor.fields import RichTextField

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    discription = RichTextField()

    class Meta:
        verbose_name = 'aboutus'
        verbose_name_plural = 'aboutus'

    def __str__(self):
        return self.title
    

class Privacy(models.Model):
    title = models.CharField(max_length=100)
    discription = RichTextField()

    class Meta:
        verbose_name = 'privacy'
        verbose_name_plural = 'privacy'

    def __str__(self):
        return self.title