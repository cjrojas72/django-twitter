from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<int:id>', views.profileview, name='profile')
]
