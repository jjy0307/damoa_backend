from .models import Article, ArticleLikes, Comment, CommentLikes
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = [
            "id",
            "user_name",
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
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = [
            "user",
            "article",
            "user_name",
            "content",
            "created_date",
            "modified_date",
        ]


class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = ["user", "comment", "likes"]
