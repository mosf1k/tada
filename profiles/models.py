from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)