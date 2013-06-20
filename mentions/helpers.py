import models


def get_entity_model(type):
    if type == 'article':
        return models.Article
    elif type == 'artist':
        return models.Artist
    elif type == 'album':
        return models.Album
    elif type == 'song':
        return models.Song
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