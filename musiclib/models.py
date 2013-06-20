# -*- coding: utf-8 -*-
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='artist_logo', blank=True, null=True)
    about = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Album(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField(blank=True, null=True)
    cover = models.ImageField(upload_to='album_cover', blank=True, null=True)
    author = models.ManyToManyField(Artist)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist)
    albums = models.ManyToManyField(Album, blank=True, null=True)
    lyrics = models.TextField(blank=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']