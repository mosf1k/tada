# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from musiclib.models import Song, Album, Artist
from news.models import Article
from datetime import datetime


class Comment(models.Model):
    """Abstract base class for Comments"""
    is_censored = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    message = models.TextField()
    publication_date = models.DateTimeField(blank=True, null=True, default=datetime.now)

    class Meta:
        abstract = True


class SongComment(Comment):
    """Represents Song Comment"""
    song = models.ForeignKey(Song)


class AlbumComment(Comment):
    """Represents Album Comment"""
    album = models.ForeignKey(Album)


class ArtistComment(Comment):
    """Represents Artist Comment"""
    artist = models.ForeignKey(Artist)


class ArticleComment(Comment):
    """Represents Article Comment"""
    article = models.ForeignKey(Article)


class Like(models.Model):
    """Abstract base class for Likes"""
    LIKE = 1
    DISLIKE = -1
    DEFAULT = 0
    LIKE_CHOICES = (
        (LIKE, 'Like'),
        (DEFAULT, 'None'),
        (DISLIKE, 'Dislike'),
    )
    user = models.ForeignKey(User)
    like_value = models.IntegerField(choices=LIKE_CHOICES, default=DEFAULT)

    class Meta:
        abstract = True


class SongLike(Like):
    """Represents Song Like"""
    song = models.ForeignKey(Song)


class AlbumLike(Like):
    """Represents Album Like"""
    album = models.ForeignKey(Album)


class ArtistLike(Like):
    """Represents Artist Like"""
    artist = models.ForeignKey(Artist)


class ArticleLike(Like):
    """Represents Article Like"""
    article = models.ForeignKey(Article)


class InfoSource(models.Model):
    """Abstract base class for Info links (links to sources of information: wiki, etc.)"""
    LAST_FM = 'lfm'
    FACEBOOK = 'fb'
    VK = 'vk'
    TWITTER = 't'
    GOOGLE_PLUS = 'g'
    WIKIPEDIA = 'wiki'
    OTHER = 'other'
    TYPE_CHOICES = (
        (LAST_FM, 'Last.fm'),
        (FACEBOOK, 'facebook'),
        (VK, u'ВКонтакте'),
        (TWITTER, 'Twitter'),
        (GOOGLE_PLUS, 'Google+'),
        (WIKIPEDIA, 'Wikipedia'),
        (OTHER, u'Другое'),
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=OTHER)
    url = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class SongInfoSource(InfoSource):
    """Represents information link for Song"""
    song = models.ForeignKey(Song)


class AlbumInfoSource(InfoSource):
    """Represents information link for Album"""
    album = models.ForeignKey(Album)


class ArtistInfoSource(InfoSource):
    """Represents information link for Artist"""
    artist = models.ForeignKey(Artist)