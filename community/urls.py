from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.MainRecommendationCommunity.as_view()),
    path("main/my_recommendation/", views.MainLoginedRecommendationCommunity.as_view()),
    path("main/my_community/", views.MainLoginedCommunity.as_view()),
    path("main/create", views.MainCreateCommunity.as_view()),
    path("invitation/request/", views.InvitationRequest.as_view()),
]
