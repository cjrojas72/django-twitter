from django.urls import path
from tweet import views

urlpatterns = [
    path('tweet/', views.AddTweet),
    path('tweetview/<int:id>', views.TweetView),
]
