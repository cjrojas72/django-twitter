from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from twitteruser.models import CustUser
from twitterclone.settings import AUTH_USER_MODEL


def index(request):
    if request.user.is_authenticated:
        return render(request, 'pages/index.html')
    else:
        return HttpResponseRedirect(reverse('login'))


def profileview(request, id):
    twitter_user = CustUser.objects.get(id=id)
    return render(request, 'pages/profile.html', {'profile': twitter_user})
