# -*- coding: utf-8 -*-
from django import template
from controls.templatetags import MENU_LIST, PAGING_COUNT
from django.conf import settings
from mentions.views import get_comment_model, get_like_model
from mentions.models import InfoSource, Like


register = template.Library()


@register.inclusion_tag('controls/menu.html')
def show_menu(current):
    return {'links': MENU_LIST, 'current': current}


@register.inclusion_tag('controls/userbar.html', takes_context=True)
def user_bar(context):
        return {'user': context['request'].user}


@register.inclusion_tag('controls/like.html', takes_context=True)
def liker(context, type, item_id):
    user_id = context['request'].user.id
    data = {'type': type, 'item_id': item_id}
    like_model = get_like_model(type)
    like = like_model.objects.filter(**{'user_id__exact': user_id, type + '_id__exact': item_id})
    if like:
        if like[0].like_value == Like.LIKE:
            data['state'] = 'like'
        elif like[0].like_value == Like.DISLIKE:
            data['state'] = 'dislike'
    else:
        data['state'] = None
    item_likes = like_model.objects.only('like_value').filter(**{type + '_id__exact': item_id})
    likes = 0
    dislikes = 0
    for item in item_likes:
        if item.like_value == Like.LIKE:
            likes += 1
        elif item.like_value == Like.DISLIKE:
            dislikes += 1
    data['likes'] = (likes, dislikes)
    return data


@register.inclusion_tag('controls/comments.html', takes_context=True)
def commenter(context, type, item_id):
    comment_model = get_comment_model(type)
    comments = comment_model.objects.filter(**{'is_censored': False, type + '_id': item_id}).order_by('publication_date')
    return {'type': type, 'item_id': item_id, 'comments': comments}


@register.inclusion_tag('controls/tags.html')
def tags(title, tags, url):
    return {'title': title, 'tags': tags, 'url': url}


@register.simple_tag
def media_url():
    return settings.MEDIA_URL


@register.inclusion_tag('controls/photo_viewer.html')
def images(image_list):
    return {'image_list': image_list}


@register.inclusion_tag('controls/paging.html')
def paging(link_prefix, total_pages, page):
    side = int(PAGING_COUNT / 2)
    page = int(page)
    pages = []
    start_index = 1
    if total_pages:
        if total_pages <= PAGING_COUNT:
            end_index = total_pages
        elif page - side <= 1:
            end_index = PAGING_COUNT - 1
        elif page + side >= total_pages:
            start_index = total_pages - PAGING_COUNT + 2
            end_index = total_pages
        else:
            start_index = page - side + 1
            end_index = page + side - 1
        if start_index != end_index:
            pages = range(start_index, end_index + 1)
    return {
        'link_prefix': link_prefix,
        'pages': pages,
        'last_index': total_pages,
        'page': page,
        'left': pages and page != 1,
        'right': pages and page != total_pages
    }

@register.filter
def subtract(value, arg):
    return value - arg


@register.inclusion_tag('controls/letter_index.html')
def letters_index(link_prefix, letters, current_letter=None):
    return {'link_prefix': link_prefix, 'letters': letters, 'current_letter': current_letter}


@register.simple_tag
def source_icon_class(type):
    if type == InfoSource.FACEBOOK:
        return 'icon-facebook'
    if type == InfoSource.GOOGLE_PLUS:
        return 'icon-gplus'
    if type == InfoSource.LAST_FM:
        return 'icon-lastfm'
    if type == InfoSource.TWITTER:
        return 'icon-twitter'
    if type == InfoSource.VK:
        return 'icon-vk'
    if type == InfoSource.WIKIPEDIA:
        return 'icon-wikipedia'
    return 'icon-link'


@register.inclusion_tag('controls/list_items.html')
def list_items(items, url_format):
    return {'items': items, 'url_format': url_format}


@register.inclusion_tag('controls/list_items.html')
def list_likes(likes, url_format):
    for like in likes:
        print like.likes_value
    return {'items': likes, 'url_format': url_format}