from .models import Article, ArticleLikes, Comment, CommentLikes
from user.models import CustomUser
from rest_framework import serializers


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "noticeboard", "user", "title", "content", "created_date"]


class ArticleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "noticeboard",
            "user",
            "title",
            "content",
            "created_date",
            "modified_date",
            "image",
            "file",
        ]


class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = ["user", "artcle", "likes"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "content", "created_date", "modified_date"]


class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = ["user", "comment", "likes"]
