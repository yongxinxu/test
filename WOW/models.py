from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.template.defaultfilters import slugify
from django.contrib import admin

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = RichTextField()
    files = models.FileField(upload_to='media/')
    url = models.URLField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    attributes = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name = models.CharField('Name', max_length=200, null=True)
    email = models.EmailField('Email', max_length=200, null=True)

    def __str__(self):
       return self.name



    
