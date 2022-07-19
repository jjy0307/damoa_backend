from .models import Article, ArticleLikes, Comment, CommentLikes
from .serializers import ArticleSerializer, ArticleLikesSerializer, CommentSerializer , CommentLikesSerializer
from rest_framework import viewsets

# 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
        
class ArticleLikesViewSet(viewsets.ModelViewSet):
    queryset = ArticleLikes.objects.all()
    serializer_class = ArticleLikesSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentLikesViewSet(viewsets.ModelViewSet):
    queryset = CommentLikes.objects.all()
    serializer_class = CommentLikesSerializer