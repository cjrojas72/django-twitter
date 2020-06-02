from django.shortcuts import render
from tweet.models import Tweet
from notification.models import Notifications
from django.utils import timezone


def notifications(request):
    user = request.user
    search_text = ('@{}').format(user)
    at_tweets = Tweet.objects.filter(body__contains=search_text)
    user_notifications = Notifications.objects.get(user=user)
    user_notifications.last_checked = timezone.now()
    user_notifications.notification_count = 0
    user_notifications.save()
    print('last checked')
    print(user_notifications.last_checked)
    return render(request, 'pages/notifications.html', {'tweets': at_tweets, 'notifications': user_notifications.notification_count})


def count_notifications(user):
    search_text = ('@{}').format(user)
    user_notifications = Notifications.objects.get(user=user)
    checked = user_notifications.last_checked
    notifications_tweets = Tweet.objects.filter(
        body__contains=search_text, date__gte=checked)
    count = len(notifications_tweets)
    user_notifications.notification_count += count
    user_notifications.save()

    return count
