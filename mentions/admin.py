from django.contrib import admin
import mentions.models


admin.site.register(mentions.models.ArtistLike)
admin.site.register(mentions.models.AlbumLike)
admin.site.register(mentions.models.SongLike)
admin.site.register(mentions.models.ArticleLike)
admin.site.register(mentions.models.SongComment)
admin.site.register(mentions.models.AlbumComment)
admin.site.register(mentions.models.ArtistComment)
admin.site.register(mentions.models.ArticleComment)
admin.site.register(mentions.models.SongInfoSource)
admin.site.register(mentions.models.AlbumInfoSource)
admin.site.register(mentions.models.ArtistInfoSource)