from community.models import Tag as TagModel, UserAndCommunity
from community.models import Community as CommunityModel
from community.models import UserAndCommunity as UserAndCommunityModel
from community.models import TagAndCommunity as TagAndCommunityModel
from rest_framework import serializers


class UserAndCommunitySerializer(serializers.ModelSerializer):
    community_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserAndCommunityModel
        fields = ["user", "community", "is_admin", "community_info"]

    def get_community_info(self, obj):
        tag_list = []
        for query in obj.community.tagandcommunity_set.all():
            tag_list.append({"name": query.tag.name})
        return {
            "name": obj.community.name,
            "is_public": obj.community.is_public,
            "image": obj.community.image.url,
            "introduction": obj.community.introduction,
            "tag": tag_list,
            "user_num": len(obj.community.userandcommunity_set.all()),
        }


class TagAndCommunitySerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TagAndCommunityModel
        fields = ["tag", "community", "tag_name"]

    def get_tag_name(self, obj):
        return {"name": obj.tag.name}


class CommunitySerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField(read_only=True)
    user_num = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CommunityModel
        fields = ["name", "is_public", "image", "introduction", "tag", "user_num"]

    def get_tag(self, obj):
        all_tag_community = obj.tagandcommunity_set.all()
        tag_list = []
        for tag_community in all_tag_community:
            tag_list.append({"name": tag_community.tag.name})
        return tag_list

    def get_user_num(self, obj):
        all_user_community = obj.userandcommunity_set.all()
        return len(all_user_community)
    

class CommunityToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityModel
        fields = ['name', 'is_public', 'image', 'introduction']      

class TagAndCommunityToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagAndCommunityModel
        fields = ['tag', 'community']

class UserAndCommunityToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndCommunityModel
        fields = ['user', 'community']    