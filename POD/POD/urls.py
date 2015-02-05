from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'POD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  
    url(r'^$', 'News.views.eventview'),
    url(r'^clan/', 'News.views.clan'),
    url(r'^', include('News.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^news/(?P<slug>\w+)/$', 'News.views.eventdetail', name='detail'),
    ##url(r'^replays/$', 'replays.views.replayslist', name='replayslist'),###
    url(r'^replays/(?P<slug>\w+)/$', 'replays.views.replayview', name='replayview'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
