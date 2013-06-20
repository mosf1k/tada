# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from musiclib.models import Song, Album, Artist
from news.models import Article
from datetime import datetime


class Comment(models.Model):
    is_censored = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    message = models.TextField()
    publication_date = models.DateTimeField(blank=True, null=True, default=datetime.now)

    class Meta:
        abstract = True


class SongComment(Comment):
    song = models.ForeignKey(Song)


class AlbumComment(Comment):
    album = models.ForeignKey(Album)


class ArtistComment(Comment):
    artist = models.ForeignKey(Artist)


class ArticleComment(Comment):
    article = models.ForeignKey(Article)


class Like(models.Model):
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
    song = models.ForeignKey(Song)


class AlbumLike(Like):
    album = models.ForeignKey(Album)


class ArtistLike(Like):
    artist = models.ForeignKey(Artist)


class ArticleLike(Like):
    article = models.ForeignKey(Article)


class InfoSource(models.Model):
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
        (VK, 'ВКонтакте'),
        (TWITTER, 'Twitter'),
        (GOOGLE_PLUS, 'Google+'),
        (WIKIPEDIA, 'Wikipedia'),
        (OTHER, 'Другое'),
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=OTHER)
    url = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class SongInfoSource(InfoSource):
    song = models.ForeignKey(Song)


class AlbumInfoSource(InfoSource):
    album = models.ForeignKey(Album)


class ArtistInfoSource(InfoSource):
    artist = models.ForeignKey(Artist)