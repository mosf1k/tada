from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj import ImageField


class UserProfile(models.Model):
    """Extends user data(i.e. with avatar image)"""
    user = models.ForeignKey(User, unique=True)
    #TODO: create screen for user account
    avatar = ImageField(blank=True, null=True)