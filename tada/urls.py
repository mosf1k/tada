from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from mentions.models import Like
from musiclib import OTHER_STARTSWITH


admin.autodiscover()

urlpatterns = patterns(
    '',
    #auth
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/register/$', 'profiles.views.register_user'),
    #news
    url(r'^$', 'news.views.articles', {'page': 1}),
    url(r'^(?P<page>\d+)/$', 'news.views.articles'),
    url(r'^article/(?P<id>\d+)/$', 'news.views.article'),
    #likes/dislikes
    url(r'^like/$', 'mentions.views.liker', {'like_value': Like.LIKE}),
    url(r'^dislike/$', 'mentions.views.liker', {'like_value': Like.DISLIKE}),
    #add comment
    url(r'^comments/add/$', 'mentions.views.add_comment'),
    #artists
    url(r'^artists/$', 'musiclib.views.artists', {'page': 1}, name='artists-base'),
    url(r'^artists/(?P<first_letter>\w)/$', 'musiclib.views.artists', {'page': 1}),
    url(r'^artists/(?P<first_letter>\w)/(?P<page>\d+)/$', 'musiclib.views.artists'),
    url(r'^artists/other/$', 'musiclib.views.artists', {'first_letter': OTHER_STARTSWITH, 'page': 1}),
    url(r'^artists/other/(?P<page>\d+)/$', 'musiclib.views.artists', {'first_letter': OTHER_STARTSWITH}),
    url(r'^artist/(?P<id>\d+)/$', 'musiclib.views.artist'),
    #album
    url(r'^album/(?P<id>\d+)/$', 'musiclib.views.album'),
    #song
    url(r'^song/(?P<id>\d+)/$', 'musiclib.views.song'),
    #tags
    url(r'^tag/(?P<id>\d+)/$', 'mentions.views.tag', name='tag-base'),
    url(r'^artists/tag/(?P<id>\d+)/$', 'mentions.views.tag', {'type': 'artist', 'page': 1}, name='artists-tag'),
    url(r'^artists/tag/(?P<id>\d+)/(?P<page>\d+)/$', 'mentions.views.tag', {'type': 'artist'}),
    url(r'^albums/tag/(?P<id>\d+)/$', 'mentions.views.tag', {'type': 'album', 'page': 1}, name='albums-tag'),
    url(r'^albums/tag/(?P<id>\d+)/(?P<page>\d+)/$', 'mentions.views.tag', {'type': 'album'}),
    url(r'^songs/tag/(?P<id>\d+)/$', 'mentions.views.tag', {'type': 'song', 'page': 1}, name='songs-tag'),
    url(r'^songs/tag/(?P<id>\d+)/(?P<page>\d+)/$', 'mentions.views.tag', {'type': 'song'}),
    url(r'^articles/tag/(?P<id>\d+)/$', 'mentions.views.tag', {'type': 'article', 'page': 1}, name='articles-tag'),
    url(r'^articles/tag/(?P<id>\d+)/(?P<page>\d+)/$', 'mentions.views.tag', {'type': 'article'}),
    #rating
    url(r'^rating/', 'mentions.views.rating', name='ratings-main'),
    url(r'^artists/rating/$', 'mentions.views.rating', {'type': 'artist', 'page': 1}, name='artists-ratings'),
    url(r'^artists/rating/(?P<page>\d+)/$', 'mentions.views.rating', {'type': 'artist'}),
    url(r'^albums/rating/$', 'mentions.views.rating', {'type': 'album', 'page': 1}, name='albums-ratings'),
    url(r'^albums/rating/(?P<page>\d+)/$', 'mentions.views.rating', {'type': 'album'}),
    url(r'^songs/rating/$', 'mentions.views.rating', {'type': 'song', 'page': 1}, name='songs-ratings'),
    url(r'^songs/rating/(?P<page>\d+)/$', 'mentions.views.rating', {'type': 'song'}),
    url(r'^articles/rating/$', 'mentions.views.rating', {'type': 'article', 'page': 1}, name='articles-ratings'),
    url(r'^articles/rating/(?P<page>\d+)/$', 'mentions.views.rating', {'type': 'article'}),
    #about
    url(r'^about/$', 'news.views.about'),
    #admin && admindocs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if not settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
