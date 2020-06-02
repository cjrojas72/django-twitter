from django.db import models
from twitteruser.models import TweetUser
from django.utils import timezone


class Notifications(models.Model):
    user = models.ForeignKey(TweetUser, on_delete=models.CASCADE)
    notification_count = models.IntegerField(default=0)
    last_checked = models.DateTimeField(default=timezone.now)
