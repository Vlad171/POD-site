from django.conf.urls import patterns, url, include

from News import views


urlpatterns = patterns('',

   url(r'^$', views.eventview, name='eventview'),
   url(r'^clan/', views.clan, name='clan' ),
   url(r'^ckeditor/', include('ckeditor.urls')),

)
