from .models import Article, ArticleLikes, Comment, CommentLikes
from rest_framework import serializers

from rest_framework.exceptions import ValidationError


class ArticleSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    noticeboard_name = serializers.SerializerMethodField()
<<<<<<< HEAD
=======
    noticeboard_id = serializers.SerializerMethodField()
>>>>>>> 5003bd8ee2d742834634b0b40935c8f0a2a178f1

    def get_user_name(self, obj):
        return obj.user.username

    def get_noticeboard_name(self, obj):
        return obj.noticeboard.name

<<<<<<< HEAD
    def get_article_count_limit(self, obj):
        return   

      
=======
    def get_noticeboard_id(self, obj):
        return obj.noticeboard.id
>>>>>>> 5003bd8ee2d742834634b0b40935c8f0a2a178f1

    class Meta:
        model = Article
        fields = [
            "id",
<<<<<<< HEAD
=======
            "noticeboard_id",
>>>>>>> 5003bd8ee2d742834634b0b40935c8f0a2a178f1
            "user",
            "user_name",
            "noticeboard",
            "noticeboard_name",
            "title",
            "content",
            "created_date",
            "modified_date",
            "image",
            "file",
        ]
<<<<<<< HEAD
        
=======

>>>>>>> 5003bd8ee2d742834634b0b40935c8f0a2a178f1
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
        if not data["image"]:
            print("image is suck", data["image"])
            raise ValidationError("image error")
        # if not data['file']:
        #     print('file is suck', data['file'])
        #     raise ValidationError('file error')
        return data


class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = ["user", "artcle", "likes"]


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    try:
        # user_name 댓글 작성시 없으면 오류나요
        def get_user_name(self, obj):
            return obj.user.username

    except AttributeError:
        # user.username = "탈퇴한 유저"
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
            "image",
            "file",
        ]