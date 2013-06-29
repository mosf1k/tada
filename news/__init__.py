from django.conf import settings


ITEMS_ON_PAGE = getattr(settings, 'ITEMS_ON_PAGE', 5)