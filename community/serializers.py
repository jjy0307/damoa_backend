from community.models import Tag as TagModel
from community.models import Community as CommunityModel
from community.models import UserAndCommunity as UserAndCommunityModel
from community.models import TagAndCommunity as TagAndCommunityModel
from rest_framework import serializers
import os

class UserAndCommunitySerializer(serializers.ModelSerializer):
    community_info = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = UserAndCommunityModel
        fields = ["user", "community", "is_admin", "community_info"]
    
    def get_community_info(self, obj):
        tag_list = []
        for query in obj.community.tagandcommunity_set.all():
            tag_list.append({'name':query.tag.name})
        return {"name" : obj.community.name, 
                "is_public" : obj.community.is_public, 
                "image" : obj.community.image.url,
                "introduction" : obj.community.introduction,
                "tag" : tag_list}
    
        


class CommunitySerializer(serializers.ModelSerializer):
    user_community_set = UserAndCommunitySerializer(many=True)
    class Meta:
        model = CommunityModel
        fields = ["name", "is_public", "image", "introduction", "user_community_set"]