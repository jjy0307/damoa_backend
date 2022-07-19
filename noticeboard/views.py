from .models import Noticeboard
from .serializers import NoticeboardSerializer
from rest_framework import viewsets

class NoticeboardViewSet(viewsets.ModelViewSet):
    queryset = Noticeboard.objects.all()
    serializer_class = NoticeboardSerializer