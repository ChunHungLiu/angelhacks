from django.conf.urls import patterns, include, url
from django.contrib import admin
from webapp import views
urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'webapp.views.index', name='index'),
     url(r'^message/$', 'webapp.views.getMessage', name='getMessage'),
     url(r'^webhook$', 'webapp.views.webhook', name='webhook'),
     url(r'^sendmsg$', 'webapp.views.sendmsg', name='sendmsg'),
     url(r'^uploadimg$', 'webapp.views.uploadimg', name='uploadimg'),
     url(r'^status/$', 'webapp.views.getStatus', name='getStatus'),
     url(r'^scanimg/$', 'webapp.views.scanimg', name='scanimg'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
