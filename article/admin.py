from django.contrib import admin
from article import models

# Register your models here.
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    """Article Admin Definition"""

    list_display = (
        "noticeboard",
        "user",
        "title",
        "content",
        "created_date",
        "modified_date",
        "image",
        "file",
    )

    ordering = (
        "noticeboard",
        "user",
        "title",
        "content",
        "created_date",
        "modified_date",
    )

    list_filter = (
        "noticeboard",
        "user",
        "title",
        "content",
        "created_date",
        "modified_date",
    )


@admin.register(models.ArticleLikes)
class ArticleLikesAdmin(admin.ModelAdmin):
    """Article Likes Admin Definition"""

    list_display = (
        "user",
        "artcle",
        "likes",
    )

    ordering = (
        "user",
        "artcle",
        "likes",
    )

    list_filter = (
        "user",
        "artcle",
        "likes",
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment Admin Definition"""

    list_display = (
        "article",
        "user",
        "content",
        "created_date",
        "modified_date",
    )

    ordering = (
        "article",
        "user",
        "content",
        "created_date",
        "modified_date",
    )

    list_filter = (
        "article",
        "user",
        "content",
        "created_date",
        "modified_date",
    )


@admin.register(models.CommentLikes)
class CommentLikesAdmin(admin.ModelAdmin):
    """Comment Likes Admin Definition"""

    list_display = (
        "user",
        "comment",
        "likes",
    )

    ordering = (
        "user",
        "comment",
        "likes",
    )

    list_filter = (
        "user",
        "comment",
        "likes",
    )
