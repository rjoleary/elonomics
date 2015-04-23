from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from elonomics import views

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(pattern_name='games')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^games/$', views.games, name='games'),
    url(r'^games/submit/$', views.submit_game, name='submit_game'),
    url(r'^players/$', views.players, name='players'),
    url(r'^players/(?P<user_name>[\w-]+)/$', views.player, name='player'),
)
