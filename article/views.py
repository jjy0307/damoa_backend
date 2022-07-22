from .models import Article, ArticleLikes, Comment, CommentLikes
from user.models import CustomUser
from .serializers import (
    ArticleListSerializer,
    ArticleUserSerializer,
    ArticleSerializer,
    ArticleLikesSerializer,
    CommentSerializer,
    CommentLikesSerializer,
)

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = ArticleUserSerializer(users, many=True)
        return Response(serializer.data)


class ArticleAdd(APIView):
    def post(self, request):
        pass


class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


# article 수정하기
class ArticleMod(APIView):
    def put(self, request):
        pass


# article 삭제하기
class ArticleDel(APIView):
    def delete(self, request):
        pass


class CommentList(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentMod(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Comment = self.get_object(pk)
        serializer = CommentSerializer(Comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDel(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Comment = self.get_object(pk)
        serializer = CommentSerializer(Comment)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleLikesDetail(APIView):
    def get_object(self, pk):
        try:
            return ArticleLikes.objects.get(pk=pk)
        except ArticleLikes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        articleLikes = self.get_object(pk)
        serializer = ArticleLikesSerializer(articleLikes)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleLikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        articleLikes = self.get_object(pk)
        serializer = ArticleLikesSerializer(articleLikes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentLikesDetail(APIView):
    def get_object(self, pk):
        try:
            return CommentLikes.objects.get(pk=pk)
        except CommentLikes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        commentLikes = self.get_object(pk)
        serializer = CommentLikesSerializer(commentLikes)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentLikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        commentLikes = self.get_object(pk)
        serializer = CommentLikesSerializer(commentLikes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass
