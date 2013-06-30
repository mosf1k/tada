# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse


PAGING_COUNT = getattr(settings, 'PAGING_COUNT', 5)

MENU_LIST = getattr(settings, 'MENU_LIST', (
    ('news', u'Новости', reverse('news.views.articles')),
    ('artists', u'Исполнители', reverse('artists-base')),
    ('ratings', u'Рейтинги', reverse('ratings-main')),
    ('about', u'О проекте', reverse('news.views.about')),
))