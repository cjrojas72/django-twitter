from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from twitterclone.settings import AUTH_USER_MODEL
from authentication.forms import LoginForm, SignUpForm
from twitteruser.models import TweetUser
from notification.models import Notifications


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TweetUser.objects.create_user(
                username=data["username"],
                password=data['password'],
                email=data['email'],
                bio=data['bio']
            )
            Notifications.objects.create(
                user=user,
                notification_count=0
            )
            return HttpResponseRedirect(reverse('login'))
    form = SignUpForm
    return render(request, 'signup.html', {'form': form})
