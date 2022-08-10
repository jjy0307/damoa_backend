from community.models import Tag as TagModel, UserAndCommunity
from community.models import Community as CommunityModel
from community.models import UserAndCommunity as UserAndCommunityModel
from community.models import TagAndCommunity as TagAndCommunityModel
from community.models import UserAndCommunityInvitation as UserAndCommunityInvitationModel
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
        fields = ["name", "is_public", "image", "introduction"]


class TagAndCommunityToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagAndCommunityModel
        fields = ["tag", "community"]


class UserAndCommunityToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndCommunityModel
        fields = ["user", "community"]


class CommunitySerializerForMyPage(serializers.ModelSerializer):
    community_name = serializers.SerializerMethodField()

    def get_community_name(self, obj):
        return obj.community.name

    class Meta:
        model = UserAndCommunity
        fields = ["id", "user", "community", "community_name"]

class ForMyPageCommunitySerialzer(serializers.ModelSerializer):
    community_name = serializers.SerializerMethodField()
    community_request = serializers.SerializerMethodField()
    
    def get_community_name(self, obj):
        return obj.community.name
    
    def get_community_request(self, obj):
        data = []
        for que in obj.community.userandcommunityinvitation_set.all():
            dic_ = {}
            dic_['id'] = que.id
            dic_['user'] = que.user.user_id
            dic_['community'] = que.community.name
            dic_['invited'] = que.invited
            dic_['request'] = que.request
            dic_['reject'] = que.reject
            dic_['accept'] = que.accept
            dic_['date'] = que.date
            data.append(dic_)
        return data
    
    class Meta:
        model = UserAndCommunityModel
        fields = ["community", "community_name", "community_request", "is_admin"]
        
class ForMyPageCommunityInvitationSerializer(serializers.ModelSerializer):
    community_name = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    community_is_admin = serializers.SerializerMethodField()
    
    def get_community_name(self, obj):
        return obj.community.name
    
    def get_user_id(self, obj):
        return obj.user.user_id
    
    def get_community_is_admin(self, obj):
        return obj.community.userandcommunity_set.get(community=obj.community.id).is_admin
    
    class Meta:
        model = UserAndCommunityInvitationModel
        fields = ['id', 'user_id', 'community_name', 'invited','request','reject','accept','date', 'community_is_admin']

class UserAndCommunityInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndCommunityInvitationModel
        fields = '__all__'