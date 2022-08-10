from django.contrib import admin
from community import models

# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag Admin Definition"""

    list_display = ("name",)

    ordering = ("name",)

    list_filter = ("name",)


# Register your models here.
@admin.register(models.TagAndCommunity)
class TagAndCommunityAdmin(admin.ModelAdmin):
    """Tag And Community Admin Definition"""

    list_display = ("tag", "community")

    ordering = ("tag", "community")

    list_filter = ("tag", "community")


@admin.register(models.Community)
class CommunityAdmin(admin.ModelAdmin):
    """Community Admin Definition"""

    list_display = (
        "name",
        "is_public",
        "image",
        "introduction",
        "created_date",
        "modified_date",
    )

    ordering = (
        "name",
        "is_public",
        "image",
        "introduction",
        "created_date",
        "modified_date",
    )

    list_filter = (
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


@admin.register(models.IpAndCommunity)
class UserAndIpAdmin(admin.ModelAdmin):
    """User And Community Admin Definition"""

    list_display = ("community", "ip")

    ordering = ("community", "ip")

    list_filter = ("community", "ip")


@admin.register(models.UserAndCommunityInvitation)
class UserAndCommunityInvitationAdmin(admin.ModelAdmin):
    list_display = ('user', 'community', 'reject', 'accept', 'date')