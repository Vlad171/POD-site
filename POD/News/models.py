from django.db import models
from django.db.models import permalink
import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

fs=FileSystemStorage(location='/media/photos')

class Event(models.Model):
    titleEvent=models.CharField(max_length=200)
    bodyEvent=models.TextField()
    author = models.ForeignKey(User, blank=True, null=True)
    slug = models.SlugField(('slug'), unique=True)
    publish = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    eventPhoto=models.ForeignKey('Photo', blank=True,null=True)

    def __unicode__(self):
        return u'%s' % self.titleEvent
    @permalink
    def get_absolute_url(self):
        return ('eventviews', None, {'slug': self.slug})

class Photo(models.Model):
    photo= models.ImageField(storage=fs)

