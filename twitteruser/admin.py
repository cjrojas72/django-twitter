from django.contrib import admin
from twitteruser.models import CustUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(CustUser, UserAdmin)
