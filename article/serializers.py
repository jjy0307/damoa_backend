from .models import Article, ArticleLikes, Comment, CommentLikes, ArticleAndImage
from rest_framework import serializers

from rest_framework.exceptions import ValidationError


class ArticleSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    noticeboard_name = serializers.SerializerMethodField()
    noticeboard_id = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        # if AttributeError:
        #     pass
        # else:
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
        ]

    def validate(self, data):
        if not data["noticeboard"]:
            print("noticebaord is suck", data["noticeboard"])
            raise ValidationError("noticeboard error")
        # if not data['user']:
        #     print('user is suck', data['user'])
        #     raise ValidationError('user error')
        if not data["title"]:
            print("title is suck", data["title"])
            raise ValidationError("title error")
        if not data["content"]:
            print("content is suck", data["content"])
            raise ValidationError("content error")
        # if not data['created_date']:
        #     print('created_date is suck', data['created_date'])
        #     raise ValidationError('created_date error')
        # if not data['modified_date']:
        #     print('modified_date is suck', data['modified_date'])
        #     raise ValidationError('modified_date error')
        # if not data["image"]:
        # print("image is suck", data["image"])
        # raise ValidationError("image error")
        # if not data['file']:
        #     print('file is suck', data['file'])
        #     raise ValidationError('file error')
        return data


class ArticleAndImageSerializer(serializers.ModelSerializer):
    article_id = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    def get_article_id(self, obj):
        return obj.article.id

    def get_image_url(self, obj):
        return obj.image.image

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


class ArticleSerializerForNoticeboard(serializers.ModelSerializer):
    # user_name = serializers.SerializerMethodField()

    # def get_user_name(self, obj):
    #     return obj.user.username

    class Meta:
        model = Article
        fields = [
            "id",
            "noticeboard",
            "user",
            "title",
            "content",
            "created_date",
            "modified_date",
            "file",
        ]
