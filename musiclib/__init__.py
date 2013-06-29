from django.conf import settings


ITEMS_ON_PAGE = getattr(settings, 'ITEMS_ON_PAGE', 5)
OTHER_STARTSWITH = 'other'
LETTERS_LIST = [chr(i) for i in xrange(ord('a'), ord('z')+1)] + [OTHER_STARTSWITH]