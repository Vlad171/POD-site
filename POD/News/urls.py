from django.conf.urls import patterns, url

from News import views

urlpatterns = patterns('',

   url(r'^$', views.index, name='index'),
   url(r'^clan/', views.clan, name='clan' ),
)