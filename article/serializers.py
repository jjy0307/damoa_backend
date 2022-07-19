from .models import Article, ArticleLikes, Comment, CommentLikes
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['noticeboard', 'user', 'title','content', 'created_date', 'modified_date', 'image','file']
        
class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = ['user', 'artcle', 'likes']
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'user', 'content', 'created_date', 'modified_date']
        
        
class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = ['user', 'comment', 'likes']