# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Song, Artist, Album
from news.models import Article
from mentions.models import ArtistInfoSource, AlbumInfoSource, SongInfoSource
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_GET
from musiclib import ITEMS_ON_PAGE, OTHER_STARTSWITH, LETTERS_LIST
import math
from django.core.urlresolvers import reverse


@require_GET
def artists(request, page, first_letter=None):
    current_page = int(page)
    if not first_letter:
        first_letter = LETTERS_LIST[0]
    first_letter = first_letter.lower()
    if first_letter == OTHER_STARTSWITH:
        filter_query = {'name__regex': '^[^A-Za-z]'}
    else:
        filter_query = {'name__istartswith': first_letter}
    query_set = Artist.objects.only('name').order_by('name').filter(**filter_query)
    total_count = query_set.count()
    artist_list = query_set[(current_page - 1) * ITEMS_ON_PAGE:current_page * ITEMS_ON_PAGE]
    paging_path = reverse('musiclib.views.artists', kwargs={'first_letter': first_letter})
    return render_to_response(
        'musiclib/artists.html',
        dict(artists=artist_list, letters=LETTERS_LIST, letter=first_letter, paging_path=paging_path,
             page=page, total_pages=int(math.ceil(float(total_count) / ITEMS_ON_PAGE))),
        context_instance=RequestContext(request)
    )


@require_GET
def artist(request, id):
    try:
        cur_artist = Artist.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404()
    albums = Album.objects.only('title', 'cover', 'publication_date').filter(author=cur_artist)
    news = Article.objects.only('publication_date', 'title').filter(is_active=True, artists_mentioned=cur_artist)[:ITEMS_ON_PAGE]
    links = ArtistInfoSource.objects.filter(artist=cur_artist)
    return render_to_response(
        'musiclib/artist.html',
        {'artist': cur_artist, 'albums': albums, 'news': news, 'links': links},
        context_instance=RequestContext(request)
    )


@require_GET
def album(request, id):
    try:
        cur_album = Album.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404()
    songs = Song.objects.only('title', 'duration').filter(albums=cur_album)
    news = Article.objects.only(
        'publication_date', 'title'
    ).filter(is_active=True, albums_mentioned=cur_album)[:ITEMS_ON_PAGE]
    links = AlbumInfoSource.objects.filter(album=cur_album)
    return render_to_response(
        'musiclib/album.html',
        {'album': cur_album, 'songs': songs, 'news': news, 'links': links},
        context_instance=RequestContext(request)
    )


@require_GET
def song(request, id):
    try:
        cur_song = Song.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404()
    albums = cur_song.albums.all()
    news = cur_song.article_set.only(
        'publication_date', 'title'
    ).filter(is_active=True, songs_mentioned=cur_song)[:ITEMS_ON_PAGE]
    links = SongInfoSource.objects.filter(song=cur_song)
    return render_to_response(
        'musiclib/song.html',
        {'song': cur_song, 'albums': albums, 'news': news, 'links': links},
        context_instance=RequestContext(request)
    )