from ast import For
from community.models import UserAndCommunityInvitation
from user.models import CustomUser as CustomUserModel
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from article.serializers import ForMyPageArticleSerializer, ForMyPageCommentSerializer
from community.serializers import ForMyPageCommunitySerialzer, ForMyPageCommunityInvitationSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ["user_id", "password", "username"]

        extra_kwarge = {
            "password": {"write_only": True},
            "user_id": {"required": "아이디를 작성해주세요", "invalid": "이미 존재하는 아이디입니다"},
            "username": {"required": "이름을 작성해주세요"},
        }

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user


# 커스텀 해서 발생하는 문제
class CustomUserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["id"] = user.id
        token["username"] = user.username
        return token

class MyPageSerializer(serializers.ModelSerializer):
    userandcommunity_set = ForMyPageCommunitySerialzer(many=True, read_only=True)
    article_set = ForMyPageArticleSerializer(many=True, read_only=True)
    comment_set = ForMyPageCommentSerializer(many=True, read_only=True)
    userandcommunityinvitation_set = ForMyPageCommunityInvitationSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomUserModel
        fields = ["user_id", "username", "created_date", "userandcommunity_set", "userandcommunityinvitation_set", "comment_set", "article_set"]