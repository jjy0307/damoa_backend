from .models import Noticeboard, UserAndNoticeboard
from rest_framework import serializers
from article.serializers import ArticleSerializerForNoticeboard


class NoticeboardSerializer(serializers.ModelSerializer):
    article_set = serializers.SerializerMethodField()
    community_name = serializers.SerializerMethodField()

    def get_article_set(self, instance):
        articles = instance.article_set.all().order_by("-created_date")
        return ArticleSerializerForNoticeboard(articles, many=True).data

    def get_community_name(self, obj):
        return obj.community.name
    class Meta:
        model = Noticeboard
        fields = [
            "id",
            "community",
            "community_name",
            "name",
            "is_public",
            "created_date",
            "modified_date",
            "article_set",
        ]


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