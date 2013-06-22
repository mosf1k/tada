from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Extends user data(i.e. with avatar image)"""
    user = models.ForeignKey(User, unique=True)
    #TODO: create screen for user account
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)