from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.loginview, name="login"),
    path('logout/', views.logoutview, name="logout"),
    path('signup/', views.signupview, name="signup")
]
