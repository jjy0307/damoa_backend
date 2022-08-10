from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("signup/", views.UserView.as_view()),
    path("login/", views.JwtTokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("mypage/", views.MyPage.as_view()),
]
