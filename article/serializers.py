from asyncore import read
from .models import Article, ArticleLikes, Comment, CommentLikes, ArticleAndImage
from rest_framework import serializers
from django.core.exceptions import ValidationError

class ArticleSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    noticeboard_name = serializers.SerializerMethodField()
    noticeboard_id = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    def get_user_name(self, obj):
        return obj.user.username

    def get_noticeboard_name(self, obj):
        return obj.noticeboard.name

    def get_noticeboard_id(self, obj):
        return obj.noticeboard.id

    def get_comment_count(self, obj):
            return obj.comment_set.count()    

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
            "count",
            "comment_count",
        ]

    def validate(self, data):
        if not data["noticeboard"]:
            print("noticebaord is suck", data["noticeboard"])
            raise ValidationError("noticeboard error")
        if not data["title"]:
            print("title is suck", data["title"])
            raise ValidationError("title error")
        if not data["content"]:
            print("content is suck", data["content"])
            raise ValidationError("content error")
        return data


   
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
class ArticleSerializerForMyPage(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    user_email = serializers.SerializerMethodField()
    user_created_date = serializers.SerializerMethodField()
    noticeboard_name = serializers.SerializerMethodField()
    noticeboard_id = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return obj.user.username

    def get_user_id(self, obj):
        return obj.user.user_id

    def get_user_email(self, obj):
        return obj.user.user_email

    def get_user_created_date(self, obj):
        return obj.user.created_date

    def get_noticeboard_name(self, obj):
        return obj.noticeboard.name

    def get_noticeboard_id(self, obj):
        return obj.noticeboard.id

    class Meta:
        model = Article
        fields = [
            "id",
            "user",
            "user_id",
            "user_name",
            "user_email",
            "user_created_date",
            "title",
            "created_date",
            "noticeboard_name",
            "noticeboard_id",
        ]
