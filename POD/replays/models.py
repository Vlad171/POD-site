from django.db import models
from django.db.models import permalink
import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import admin
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Replay(models.Model):
    replaytitle=models.CharField(max_length=200)
    html=models.CharField(max_length=400)
    description=RichTextField()
    authorreplay = models.ForeignKey(User, blank=True, null=True)
    slug = models.SlugField(('slug'), unique=True)
    publishreplay = models.DateTimeField(default=datetime.datetime.now)
    createdreplay = models.DateTimeField(auto_now=True)
    modifiedreplay = models.DateTimeField(auto_now_add=True)	

    class Meta:
        verbose_name = ('replay')

    def __unicode__(self):
        return u'%s' % self.replaytitle