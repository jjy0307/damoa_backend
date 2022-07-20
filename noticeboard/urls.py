from django.urls import path, include
from .views import NoticeboardViewSet, UserAndNoticeboardViewSet

# 게시판 보기, 생성
noticeboard_create = NoticeboardViewSet.as_view({"get": "list", "post": "create"})

# UserAndNoticeboard 클래스 보기
noticeboard_create_list = UserAndNoticeboardViewSet.as_view(
    {
        "get": "list",
    }
)


urlpatterns = [
    path("noticeboard/create/", noticeboard_create),
    path("noticeboard/create/list", noticeboard_create_list),
]
