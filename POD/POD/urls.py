from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'POD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  
    url(r'^$', 'News.views.index'),
    url(r'^clan/', 'News.views.clan'),
    url(r'^News/', include('News.urls', namespace='News')),
    url(r'^admin/', include(admin.site.urls)),
)
