from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class TweetUser(AbstractUser):
    bio = models.TextField()
    following = models.ManyToManyField(
        'self', through='UserConnect', symmetrical=False, related_name='relationships')
    created_on = models.DateTimeField(default=timezone.now)


class UserConnect(models.Model):
    owner = models.ForeignKey(
        TweetUser, on_delete=models.CASCADE, related_name='owner')
    target = models.ForeignKey(
        TweetUser, on_delete=models.CASCADE, related_name='target')
