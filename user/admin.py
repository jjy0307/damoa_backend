from django.contrib import admin
from user import models

# Register your models here.
@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Custom User Admin Definition"""

    list_display = (
        "user_id",
        # "user_email",
        "password",
        "username",
        "created_date",
        "is_active",
        "is_admin",
    )

    ordering = ("user_id", "username", "created_date", "is_admin")

    list_filter = (
        "user_id",
        # "user_email",
        "password",
        "username",
        "created_date",
        "is_active",
        "is_admin",
    )
