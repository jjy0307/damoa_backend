from .models import Article, ArticleLikes, Comment, CommentLikes, ArticleAndImage
from datetime import date, datetime, timedelta
from .serializers import (
    ArticleSerializer,
    ArticleLikesSerializer,
    CommentSerializer,
    CommentLikesSerializer,
    ArticleAndImageSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

class ArticleAdd(APIView):
    def get(self, request):
        articles = Article.objects.all
        serializer = ArticleSerializer(articles, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    # def post(self, request):
    #     # print('request.data', request.data)
    #     notice_board = Noticeboard.objects.get(name="공개게시판")
    #     print(request.data)
    #     # print("notice_board", notice_board)
    #     data2 = copy.deepcopy(request.data)
    #     # print("data2", data2)
    #     data2["noticeboard"] = notice_board.id
    #     # print("data2['noticeboard']", data2['noticeboard'])
    #     # print("data2", data2)
    #     serializer = ArticleSerializer(data=data2)
    #     print("1")
    #     if serializer.is_valid():
    #         print("1")
    #         serializer.save()
    #         return Response({"message": "글 작성 완료!!"})
    #     return Response({"message": f"${serializer.errors}"}, 400)


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


class ArticleMod(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDel(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleAndImageList(APIView):
    def get(self, request):
        images = ArticleAndImage.objects.all()
        serializer = ArticleAndImageSerializer(images, many=True)
        return Response(serializer.data)


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

class Article_Comment(APIView):
     def get(self, request, pk):
        comments = Comment.objects.filter(article_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)   


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