from .models import Noticeboard, UserAndNoticeboard
from rest_framework import serializers

class NoticeboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticeboard
        fields = ['community', 'name', 'is_public', 'created_date', 'modified_date']
        
class UserAndNoticeboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndNoticeboard
        fields = ['user', 'noticeboard', 'is_creator', 'date_joined']
        