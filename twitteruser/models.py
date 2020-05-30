from django.db import models
from django.contrib.auth.models import AbstractUser


class CustUser(AbstractUser):
    display_name = models.CharField(max_length=50)
    tweets = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    REQUIRED_FIELDS = ['display_name']
