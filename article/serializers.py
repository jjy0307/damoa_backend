from asyncore import read
from .models import Article, ArticleLikes, Comment, CommentLikes, ArticleAndImage
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ArticleSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    noticeboard_name = serializers.SerializerMethodField()
    noticeboard_id = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    def get_user_name(self, obj):
        # if AttributeError:
        #     pass
        # else:
        return obj.user.username

    def get_noticeboard_name(self, obj):
        # if AttributeError:
        #     pass
        # else:
        return obj.noticeboard.name

    def get_noticeboard_id(self, obj):
        # if AttributeError:
        #     pass
        # else:
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


    # def validate(self, data):
    #     if not data["noticeboard"]:
    #         print("noticebaord is suck", data["noticeboard"])
    #         raise ValidationError("noticeboard error")
    #     # if not data['user']:
    #     #     print('user is suck', data['user'])
    #     #     raise ValidationError('user error')
    #     if not data["title"]:
    #         print("title is suck", data["title"])
    #         raise ValidationError("title error")
    #     if not data["content"]:
    #         print("content is suck", data["content"])
    #         raise ValidationError("content error")
    #     # if not data['created_date']:
    #     #     print('created_date is suck', data['created_date'])
    #     #     raise ValidationError('created_date error')
    #     # if not data['modified_date']:
    #     #     print('modified_date is suck', data['modified_date'])
    #     #     raise ValidationError('modified_date error')
    #     # if not data["image"]:
    #     # print("image is suck", data["image"])
    #     # raise ValidationError("image error")
    #     # if not data['file']:
    #     #     print('file is suck', data['file'])
    #     #     raise ValidationError('file error')
    #     return data


class ArticleAndImageSerializer(serializers.ModelSerializer):
    article_id = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    def get_article_id(self, obj):
        return obj.article.id

    def get_image_url(self, obj):
        # print(f"이미지는...{obj.image.url}")
        # print(dir(obj.image.image))
        return obj.image.url

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
class ArticleAndImageToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAndImage
        fields = ['article', 'image']
        
class ArticleToolSerializer(serializers.ModelSerializer):
    images = ArticleAndImageToolSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ['images', 'noticeboard', 'user', 'title', 'content', 'file', 'is_valid']
    def create(self, validate_data):
        instance = Article.objects.create(**validate_data)
        image = self.context
        for image_data in image:
            ArticleAndImage.objects.create(article=instance, image=image[image_data])
        return instance

        