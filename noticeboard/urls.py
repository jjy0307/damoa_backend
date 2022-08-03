from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("create/", views.NoticeboardList.as_view()),
    path("create/<int:pk>/", views.NoticeboardDetail.as_view()),
    path("view/<int:pk>/", views.NoticeboardObject.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
