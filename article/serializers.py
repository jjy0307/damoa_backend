from asyncore import read
from .models import Article, ArticleLikes, Comment, CommentLikes, ArticleAndImage
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ArticleSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    noticeboard_name = serializers.SerializerMethodField()
    noticeboard_id = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return obj.user.username

    def get_noticeboard_name(self, obj):
        return obj.noticeboard.name

    def get_noticeboard_id(self, obj):
        return obj.noticeboard.id

    class Meta:
        model = Article
        fields = [
            "id",
            "user",
            "user_name",
            "noticeboard_id",
            "noticeboard_name",
            "title",
            "content",
            "created_date",
            "modified_date",
            "file",
            "is_valid",
        ]

class ArticleAndImageSerializer(serializers.ModelSerializer):
    article_id = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    def get_article_id(self, obj):
        return obj.article.id

    def get_image_url(self, obj):
        return obj.image.image.url

    class Meta:
        model = ArticleAndImage
        fields = ["image", "article_id", "image_url"]


class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = ["user", "artcle", "likes"]


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    try:

        def get_user_name(self, obj):
            return obj.user.username

    except AttributeError:
        pass

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "article",
            "user_name",
            "content",
            "created_date",
            "modified_date",
            "is_valid",
        ]


class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = ["user", "comment", "likes"]


class ArticleSerializerForNoticeboard(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = [
            "id",
            "noticeboard",
            "user",
            "user_name",
            "title",
            "content",
            "created_date",
            "modified_date",
            "file",
            "user_name"
        ]


class ArticleAndImageToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAndImage
        fields = ["article", "image"]


class ArticleToolSerializer(serializers.ModelSerializer):
    images = ArticleAndImageToolSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            "images",
            "noticeboard",
            "user",
            "title",
            "content",
            "file",
            "is_valid",
        ]

    def create(self, validate_data):
        instance = Article.objects.create(**validate_data)
        image = self.context
        for image_data in image:
            ArticleAndImage.objects.create(article=instance, image=image[image_data])
        return instance
