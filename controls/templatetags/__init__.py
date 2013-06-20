# -*- coding: utf-8 -*-
from django.conf import settings


PAGING_COUNT = getattr(settings, 'PAGING_COUNT', 5)

MENU_LIST = getattr(settings, 'MENU_LIST', (
    ('news', u'Новости', u'/'),
    ('artists', u'Исполнители', u'/artists'),
    ('ratings', u'Рейтинги', u'/rating'),
    ('about', u'О проекте', u'/about'),
))