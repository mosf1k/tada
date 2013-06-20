from django.contrib import admin
from musiclib.models import Tag, Artist, Album, Song


admin.site.register(Tag)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
