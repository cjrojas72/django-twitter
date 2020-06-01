from django.db import models
from twitteruser.models import TweetUser
from django.utils import timezone


class Tweet(models.Model):
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    author = models.ForeignKey(TweetUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.author
