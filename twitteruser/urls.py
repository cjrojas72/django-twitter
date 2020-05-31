from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<int:id>', views.profileview, name='profile'),
    path('follow/<int:id>', views.follow, name='follow'),
    path('unfollow/<int:id>', views.unfollow, name='unfollow'),
]
