from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("noticeboard/create/", views.NoticeboardList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)