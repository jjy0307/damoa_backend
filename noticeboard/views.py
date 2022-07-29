from .models import Noticeboard
from article.models import Article
from .serializers import NoticeboardSerializer
from article.serializers import ArticleSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class NoticeboardList(APIView):
    def get(self, request):
        noticeboards = Noticeboard.objects.all()
        serializer = NoticeboardSerializer(noticeboards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoticeboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeboardDetail(APIView):
    def get(self, request, pk=None):
        query = {}
        if pk:
            query["noticeboard_id"] = pk

        serializer = ArticleSerializer(Article.objects.filter(**query), many=True)
        return Response(serializer.data)
