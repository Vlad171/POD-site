from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
# Create your models here.

fs=FileSystemStorage(location='/media/photos')

class Event(models.Model):
	titleEvent=models.CharField(max_length=200)
	bodyEvent=models.TextField()
	author = models.ForeignKey(User, blank=True, null=True)
	slug = models.SlugField(unique=True)
	publish = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    eventPhoto=ForeignKey('Photo', blank=True,null=True)

    def __unicode__(self):
        return u'%s' % self.title

class Photo(model.Model):
    photo= models.ImageField(storage=fs)

    def __unicode__(self):
        return u'%s' % self.title


