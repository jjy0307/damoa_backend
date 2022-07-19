from django.urls import path, include
from .views import NoticeboardViewSet

# 게시판 보기, 생성
noticeboard_create = NoticeboardViewSet.as_view({
    'get':'list',
    'post':'create'
})


urlpatterns = [
    path('noticeboard/create/', noticeboard_create),
]



