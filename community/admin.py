from django.contrib import admin
from community import models

# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag Admin Definition"""

    list_display = ("name",)

    ordering = ("name",)

    list_filter = ("name",)


@admin.register(models.Community)
class CommunityAdmin(admin.ModelAdmin):
    """Community Admin Definition"""

    list_display = (
        "tag",
        "name",
        "is_public",
        "image",
        "introduction",
        "created_date",
        "modified_date",
    )

    ordering = (
        "tag",
        "name",
        "is_public",
        "image",
        "introduction",
        "created_date",
        "modified_date",
    )

    list_filter = (
        "tag",
        "name",
        "is_public",
        "image",
        "introduction",
        "created_date",
        "modified_date",
    )


@admin.register(models.UserAndCommunity)
class UserAndCommunityAdmin(admin.ModelAdmin):
    """User And Community Admin Definition"""

    list_display = (
        "user",
        "community",
        "is_admin",
        "date_joined",
    )

    ordering = (
        "user",
        "community",
        "is_admin",
        "date_joined",
    )

    list_filter = (
        "user",
        "community",
        "is_admin",
        "date_joined",
    )
