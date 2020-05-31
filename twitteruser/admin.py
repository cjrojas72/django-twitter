from django.contrib import admin
from twitteruser.models import TweetUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(TweetUser, UserAdmin)
