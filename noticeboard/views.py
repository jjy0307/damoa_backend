from .models import Noticeboard, UserAndNoticeboard
from .serializers import NoticeboardSerializer, UserAndNoticeboardSerializer
from rest_framework import viewsets


class NoticeboardViewSet(viewsets.ModelViewSet):
    queryset = Noticeboard.objects.all()
    serializer_class = NoticeboardSerializer


class UserAndNoticeboardViewSet(viewsets.ModelViewSet):
    queryset = UserAndNoticeboard.objects.all()
    serializer_class = UserAndNoticeboardSerializer
