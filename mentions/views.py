# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
import models
from models import Song, Artist, Album
from news.models import Article
from django.db.models import Count, Sum
from musiclib.models import Tag
from django.http import Http404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import json
import math


ITEMS_ON_PAGE = getattr(settings, 'ITEMS_ON_PAGE', 5)


def get_entity_model(type):
    if type == 'article':
        return Article
    elif type == 'artist':
        return Artist
    elif type == 'album':
        return Album
    elif type == 'song':
        return Song
    else:
        raise ValueError('Model of such type is not exist')


def get_like_model(type):
    if type == 'article':
        return models.ArticleLike
    elif type == 'artist':
        return models.ArtistLike
    elif type == 'album':
        return models.AlbumLike
    elif type == 'song':
        return models.SongLike
    else:
        raise ValueError('Model of such type is not exist')


def get_comment_model(type):
    if type == 'article':
        return models.ArticleComment
    elif type == 'artist':
        return models.ArtistComment
    elif type == 'album':
        return models.AlbumComment
    elif type == 'song':
        return models.SongComment
    else:
        raise ValueError('Model of such type is not exist')


def liker(request, action):
    if request.method == 'POST':
        user_id = request.user.id
        like_value = models.Like.LIKE if action == 'like' else models.Like.DISLIKE
        type = request.POST['type']
        id = request.POST['item_id']
        likeModel = get_like_model(type)
        try:
            user_like = likeModel.objects.filter(**{'user_id__exact': user_id, type + '_id__exact': id})
            if user_like:
                user_like = user_like[0]
                user_like.like_value = like_value
                user_like.save()
            else:
                user_like = likeModel.objects.create(**{'like_value': like_value, 'user_id': user_id, type + '_id': id})
            item_likes = likeModel.objects.filter(**{type + '_id__exact': id}).only('like_value')
            likes = 0
            dislikes = 0
            for item in item_likes:
                if item.like_value == models.Like.LIKE:
                    likes += 1
                elif item.like_value == models.Like.DISLIKE:
                    dislikes += 1
            result = {'success': True, 'likes': likes, 'dislikes': dislikes}
        except:
            result = {'success': False}
    else:
        result = {'success': False}
    return HttpResponse(json.dumps(result), mimetype="application/json")


def add_comment(request):
    if request.method == 'POST' and request.user.is_authenticated():
        message = request.POST['text']
        type = request.POST['type']
        item_id = request.POST['item_id']
        if message and type and item_id:
            comment_model = get_comment_model(type)
            new_comment = comment_model.objects.create(**{
                'is_censored': False,
                'user_id': request.user.id,
                type + '_id': item_id,
                'message': message
            })
            comments = comment_model.objects.filter(is_censored=False).order_by('publication_date')
            return render_to_response('controls/comments_list.html', {'comments': comments})
    return HttpResponse(status=500)


def tag(request, id, type=None, page=1):
    try:
        cur_tag = Tag.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404()
    result = {'tag': cur_tag}
    if type:
        types = (type,)
    else:
        types = ('article', 'artist', 'album', 'song')
    for name in types:
        query_set = getattr(cur_tag, name + '_set').only('name' if name == 'artist' else 'title')
        if type:
            total_count = query_set.count()
            result['total_pages'] = int(math.ceil(float(total_count)/ITEMS_ON_PAGE))
            result['page'] = page
            result['paging_path'] = '/%ss/tag/%s/' % (type, id)
        current_page = int(page)
        result[name + 's'] = query_set[(current_page - 1) * ITEMS_ON_PAGE:current_page * ITEMS_ON_PAGE]
    return render_to_response('mentions/tag.html', result, context_instance=RequestContext(request))


def rating(request, type=None, page=1):
    result = {}
    if type:
        types = (type,)
    else:
        types = ('article', 'artist', 'album', 'song')
    has_response = False
    for name in types:
        model = get_entity_model(name)
        query_set = model.objects.exclude(**{
            name + 'like__like_value__isnull': True
        }).annotate(likes_value=Sum(name + 'like__like_value')).order_by('-likes_value')
        if type:
            total_count = query_set.count()
            result['total_pages'] = int(math.ceil(float(total_count)/ITEMS_ON_PAGE))
            result['page'] = page
            result['paging_path'] = '/%ss/rating/' % type
        current_page = int(page)
        result[name + 's'] = query_set[(current_page - 1) * ITEMS_ON_PAGE:current_page * ITEMS_ON_PAGE]
        if result[name + 's']:
            has_response = True
    result['empty_response'] = not has_response
    return render_to_response('mentions/rating.html', result, context_instance=RequestContext(request))