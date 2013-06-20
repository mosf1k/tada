# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Article
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
import math
from django.conf import settings


ITEMS_ON_PAGE = getattr(settings, 'ITEMS_ON_PAGE', 5)


def articles(request, page):
    articles_count = Article.objects.filter(is_active=True).count()
    current_page = int(page)
    if articles_count and page > 0:
        article_list = Article.objects.filter(is_active=True).order_by('-publication_date').only(
            'title', 'publication_date', 'tags'
        )[(current_page - 1) * ITEMS_ON_PAGE:current_page * ITEMS_ON_PAGE]
    else:
        article_list = None
    return render_to_response(
        'news/articles.html',
        dict(articles=article_list, page=page, total_pages=int(math.ceil(float(articles_count) / ITEMS_ON_PAGE))),
        context_instance=RequestContext(request)
    )


def article(request, id):
    try:
        cur_article = Article.objects.filter(is_active=True).get(id=id)
    except ObjectDoesNotExist:
        raise Http404()
    return render_to_response('news/article.html', {'article': cur_article}, context_instance=RequestContext(request))


def about(request):
    return render_to_response('about/about.html', {}, context_instance=RequestContext(request))