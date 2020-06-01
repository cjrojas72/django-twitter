from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from twitteruser.models import TweetUser, UserConnect
from twitterclone.settings import AUTH_USER_MODEL
from tweet.models import Tweet


def index(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        tweetfeed = Tweet.objects.all()
        tweetfeed = tweetfeed.order_by('-date')
        all_users = TweetUser.objects.all()
        all_users = all_users.exclude(id=user.id)
        all_users = all_users.exclude(username='admin')

        user_following = follow_list(user)
        return render(request, 'pages/index.html', {'all': all_users, 'list': user_following, 'feed': tweetfeed})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
def profileview(request, id):
    profile = TweetUser.objects.get(id=id)
    user_following = follow_list(profile)
    user_id_tuple = []

    for user in user_following:
        user_id = user.target.id
        user_id_tuple.append(user_id)

    user_id_tuple = tuple(user_id_tuple)
    print(user_id_tuple)

    tweets = Tweet.objects.filter(author__in=user_id_tuple)
    tweets.order_by('-date')

    return render(request, 'pages/profile.html', {'profile': profile, 'list': user_following, 'tweets': tweets})


def follow(request, id):
    target = TweetUser.objects.get(id=id)

    UserConnect.objects.get_or_create(
        owner=request.user,
        target=target
    )
    return HttpResponseRedirect(reverse('home'))


def unfollow(request, id):
    target = TweetUser.objects.get(id=id)

    UserConnect.objects.filter(
        owner=request.user,
        target=target
    ).delete()

    return HttpResponseRedirect(reverse('home'))


def follow_list(owner):
    following = UserConnect.objects.filter(owner=owner)

    return following


# def owner_tweets(owner):
#     twee_owner =
#     tweets = Tweet.objects.filter()
#     return tweets
