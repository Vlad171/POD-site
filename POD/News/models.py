from django.db import models
from django.db.models import permalink
import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import admin
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

fs=FileSystemStorage(location='media/')

class Event(models.Model):
    titleEvent=models.CharField(max_length=200)
    bodyEvent=RichTextField()
    author = models.ForeignKey(User, blank=True, null=True)
    slug = models.SlugField(('slug'), unique=True)
    publish = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    eventPhoto=models.ForeignKey('Photo', blank=True,null=True)
    
    class Meta:
        verbose_name = ('event')
    
    def __unicode__(self):
        return u'%s' % self.titleEvent

    @permalink
    def get_absolute_url(self):
        return ('evendetail', None, {'slug': self.slug})

class Photo(models.Model):
    photo= models.ImageField(storage=fs)

class MainPhoto(models.Model):
	mainphoto=models.ImageField(storage=fs)

