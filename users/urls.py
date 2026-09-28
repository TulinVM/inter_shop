# users/urls.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (EmailVerificationView, UserLoginView, UserProfileView, UserProfileView1,
                    UserRegistrationView, CustomLogoutView)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registr/', UserRegistrationView.as_view(), name='registration'),
    path("profile/<int:pk>", login_required(UserProfileView.as_view()), name='profile'),
    path("profile1/<int:pk>", login_required(UserProfileView1.as_view()), name='profile1'),
    path('get_absolute_url/',LogoutView.as_view(next_page='index'),name='logout'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('email_verification/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]
