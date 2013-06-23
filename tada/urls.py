from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.contrib import admin
from news.views import article, articles, about
from profiles.views import register_user
from mentions.views import liker, add_comment, tag, rating
from musiclib.views import artists, artist, album, song


admin.autodiscover()

urlpatterns = patterns(
    '',
    #auth
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register_user),
    #news
    url(r'^$', articles, {'page': 1}),
    url(r'^(?P<page>\d+)/$', articles),
    url(r'^article/(?P<id>\d+)/$', article),
    #likes/dislikes
    url(r'^like/$', liker, {'action': 'like'}),
    url(r'^dislike/$', liker, {'action': 'dislike'}),
    #add comment
    url(r'^comments/add/$', add_comment),
    #artists
    url(r'^artists/$', artists, {'page': 1}),
    url(r'^artists/(?P<first_letter>\w)/$', artists, {'page': 1}),
    url(r'^artists/(?P<first_letter>\w)/(?P<page>\d+)/$', artists),
    url(r'^artist/(?P<id>\d+)/$', artist),
    #album
    url(r'^album/(?P<id>\d+)/$', album),
    #song
    url(r'^song/(?P<id>\d+)/$', song),
    #tags
    url(r'^tag/(?P<id>\d+)/$', tag),
    url(r'^artists/tag/(?P<id>\d+)/$', tag, {'type': 'artist', 'page': 1}),
    url(r'^artists/tag/(?P<id>\d+)/(?P<page>\d+)/$', tag, {'type': 'artist'}),
    url(r'^albums/tag/(?P<id>\d+)/$', tag, {'type': 'album', 'page': 1}),
    url(r'^albums/tag/(?P<id>\d+)/(?P<page>\d+)/$', tag, {'type': 'album'}),
    url(r'^songs/tag/(?P<id>\d+)/$', tag, {'type': 'song', 'page': 1}),
    url(r'^songs/tag/(?P<id>\d+)/(?P<page>\d+)/$', tag, {'type': 'song'}),
    url(r'^articles/tag/(?P<id>\d+)/$', tag, {'type': 'article', 'page': 1}),
    url(r'^articles/tag/(?P<id>\d+)/(?P<page>\d+)/$', tag, {'type': 'article'}),
    #rating
    url(r'^rating/', rating),
    url(r'^artists/rating/$', rating, {'type': 'artist', 'page': 1}),
    url(r'^artists/rating/(?P<page>\d+)/$', rating, {'type': 'artist'}),
    url(r'^albums/rating/$', rating, {'type': 'album', 'page': 1}),
    url(r'^albums/rating/(?P<page>\d+)/$', rating, {'type': 'album'}),
    url(r'^songs/rating/$', rating, {'type': 'song', 'page': 1}),
    url(r'^songs/rating/(?P<page>\d+)/$', rating, {'type': 'song'}),
    url(r'^articles/rating/$', rating, {'type': 'article', 'page': 1}),
    url(r'^articles/rating/(?P<page>\d+)/$', rating, {'type': 'article'}),
    #about
    url(r'^about/$', about),
    #admin && admindocs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if not settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
