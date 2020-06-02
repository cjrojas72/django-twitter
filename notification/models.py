from django.db import models
from twitteruser.models import TweetUser


class Notifications(models.Model):
    user = models.ForeignKey(TweetUser, on_delete=models.CASCADE)
    notification_count = models.IntegerField(default=0)
