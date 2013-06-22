# -*- coding: utf-8 -*-
from django.db import models
from musiclib.models import Artist, Album, Song, Tag
from pyuploadcare.dj import ImageField


class ArticlePhoto(models.Model):
    """Represents photo connected to news Article"""
    title = models.CharField(max_length=50)
    image = ImageField(verbose_name=u'Изображения к новости')

    def __unicode__(self):
        return self.title


class Article(models.Model):
    """Represents Article"""
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    text = models.TextField()
    publication_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    photos = models.ManyToManyField(ArticlePhoto, blank=True, null=True)
    artists_mentioned = models.ManyToManyField(Artist, blank=True, null=True)
    albums_mentioned = models.ManyToManyField(Album, blank=True, null=True)
    songs_mentioned = models.ManyToManyField(Song, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']