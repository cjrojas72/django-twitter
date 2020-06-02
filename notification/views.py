from django.shortcuts import render
from tweet.models import Tweet
from notification.models import Notifications


def notifications(request):
    user = request.user
    search_text = ('@{}').format(user)
    at_tweets = Tweet.objects.filter(body__contains=search_text)
    user_notifications = Notifications.objects.get(user=user)
    user_notifications.notification_count = 0
    user_notifications.save()
    print(user_notifications.notification_count)
    return render(request, 'pages/notifications.html', {'tweets': at_tweets})


def count_notifications(user):
    search_text = ('@{}').format(user)
    notifications_tweets = Tweet.objects.filter(body__contains=search_text)
    count = len(notifications_tweets)
    user_notifications = Notifications.objects.get(user=user)
    user_notifications.notification_count += count
    user_notifications.save()

    return count
