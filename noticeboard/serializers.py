from .models import Noticeboard
from rest_framework import serializers

class NoticeboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticeboard
        fields = ['name']