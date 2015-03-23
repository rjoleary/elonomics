from django.conf.urls import patterns, include, url
from django.contrib import admin
from elonomics import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^players/$', views.players, name='players'),
    url(r'^players/(?P<user_name>[\w-]+)/$', views.player, name='player'),
    url(r'^history/$', views.history, name='history'),
    url(r'^matches/submit/$', views.submit_match, name='submit_match'),
    url(r'^support/$', views.support, name='support')
)
