from .models import Noticeboard, UserAndNoticeboard
from rest_framework import serializers
from article.serializers import ArticleSerializerForNoticeboard


class NoticeboardSerializer(serializers.ModelSerializer):
    # article_set = ArticleSerializerForNoticeboard(many=True, read_only=True)

    article_set = serializers.SerializerMethodField()

    def get_article_set(self, instance):
        articles = instance.article_set.all().order_by("-created_date")
        return ArticleSerializerForNoticeboard(articles, many=True).data

    # article_info = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Noticeboard
<<<<<<< HEAD

        fields = ["community", "name", "is_public", "created_date", "modified_date", "article_set"]
    # def get_article_info(self, obj):
    #     return 
=======
        fields = [
            "id",
            "community",
            "name",
            "is_public",
            "created_date",
            "modified_date",
            "article_set",
        ]


>>>>>>> 3e5d77ced11ceb269acff61b218ff3b8a99b7882
class UserAndNoticeboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndNoticeboard
        fields = ["user", "noticeboard", "is_creator", "date_joined"]


class NoticeboardandArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticeboard
        fields = [
            "id",
            "community",
            "name",
            "is_public",
            "created_date",
            "modified_date",
        ]
