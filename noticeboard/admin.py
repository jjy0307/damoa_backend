from django.contrib import admin
from noticeboard import models
# Register your models here.
@admin.register(models.Noticeboard)
class NoticeboardAdmin(admin.ModelAdmin):
    """Noticeboard Admin Definition"""
    list_display = (
        'community',
        'name',
        'is_public',
        'created_date',
        'modified_date',
    )
    
    ordering = (
        'community',
        'name',
        'is_public',
        'created_date',
        'modified_date',
    )
    
    list_filter = (
        'community',
        'name',
        'is_public',
        'created_date',
        'modified_date',
    )
    
@admin.register(models.UserAndNoticeboard)
class UserAndNoticeboardAdmin(admin.ModelAdmin):
    """User And Noticeboard Admin Definition"""
    list_display = (
        'user',
        'noticeboard',
        'is_creator',
        'date_joined',
    )
    
    ordering = (
        'user',
        'noticeboard',
        'is_creator',
        'date_joined',
    )
    
    list_filter = (
        'user',
        'noticeboard',
        'is_creator',
        'date_joined',
    )    