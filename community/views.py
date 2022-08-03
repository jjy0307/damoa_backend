from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction

from community.serializers import (
    CommunitySerializer,
    UserAndCommunitySerializer,
    CommunityToolSerializer,
    TagAndCommunityToolSerializer,
    UserAndCommunityToolSerializer,
    CommunitySerializerForMyPage,
)

from user.models import CustomUser as CustomUserModel
from community.models import Community as CommunityModel
from community.models import UserAndCommunity as UserAndCommunityModel
from community.models import Tag as TagModel

# Create your views here.
class MainLoginedCommunity(APIView):
    def get_community_count_order_list(self):
        order_data = []
        community_order_list = CommunityModel.objects.all().order_by("-count")
        count_num = 0
        for community_query in community_order_list:
            order_data.append(
                {"community": community_query.name, "count": community_query.count}
            )
            if count_num == 4:
                break
            count_num += 1
        return order_data

    def get(self, request):
        user = request.user
        data = {}
        if user.is_anonymous:
            public_community = CommunityModel.objects.filter(is_public=True)
            serializer = CommunitySerializer(public_community, many=True)
            data["community"] = serializer.data
            data["tag"] = []
            for s_datas in serializer.data:
                for s_data in s_datas["tag"]:
                    if s_data["name"] not in data["tag"]:
                        data["tag"].append(s_data["name"])
            data[
                "community_hit_count"
            ] = MainLoginedCommunity.get_community_count_order_list(self)
            return Response(data, status=200)

        user_community = UserAndCommunityModel.objects.filter(user=request.user)
        user_community_serializer = UserAndCommunitySerializer(
            user_community, many=True
        )
        data["community"] = user_community_serializer.data
        data["tag"] = []
        for s_datas in user_community_serializer.data:
            for s_data in s_datas["community_info"]["tag"]:
                if s_data["name"] not in data["tag"]:
                    data["tag"].append(s_data["name"])
        data["all_tag"] = []
        for tag_data in TagModel.objects.all():
            data["all_tag"].append(tag_data.name)

        data[
            "community_hit_count"
        ] = MainLoginedCommunity.get_community_count_order_list(self)
        return Response(data, status=200)


class MainCreateCommunity(APIView):
    def community_data(self, data):
        community_data = {}
        community_data["name"] = data["name"]
        community_data["is_public"] = data["is_public"]
        community_data["image"] = data["image"]
        community_data["introduction"] = data["introduction"]
        return community_data

    def tag_and_community_data(self, tag, data):
        tag_and_community_data = {}
        tag_and_community_data["tag"] = TagModel.objects.get(name=tag).id
        tag_and_community_data["community"] = CommunityModel.objects.get(
            name=data["name"]
        ).id
        return tag_and_community_data

    def user_and_community_data(self, data):
        user_info = eval(data["user_id"])
        user_and_community_data = {}
        user_and_community_data["user"] = CustomUserModel.objects.get(
            username=user_info["username"]
        ).id
        user_and_community_data["community"] = CommunityModel.objects.get(
            name=data["name"]
        ).id
        return user_and_community_data

    @transaction.atomic
    def post(self, request):
        if not request.data["name"]:
            return Response({"message": "name_none"})
        if CommunityModel.objects.filter(name=request.data["name"]):
            return Response({"message": "name_exist"}, status=400)
        if not request.data["introduction"]:
            return Response({"message": "introduction"}, status=400)
        if request.data["image"] == "undefined":
            return Response({"message": "image"}, status=400)
        make_community_serializer = CommunityToolSerializer(
            data=MainCreateCommunity.community_data(self, request.data)
        )
        if make_community_serializer.is_valid():
            make_community_serializer.save()

        if request.data['tags']:
            for tag in request.data['tags'].split(','):
                make_tag_and_community_serializer = TagAndCommunityToolSerializer(data=MainCreateCommunity.tag_and_community_data(self, tag, request.data))        
                if make_tag_and_community_serializer.is_valid():
                    make_tag_and_community_serializer.save()
        
        make_user_and_community_serializer = UserAndCommunitySerializer(data=MainCreateCommunity.user_and_community_data(self, request.data))
        if make_user_and_community_serializer.is_valid():
            make_user_and_community_serializer.save()
        return Response({"message": "성공적으로 완성되었습니다"}, status=200)


class MypageForCommunity(APIView):
    def get(self, request):
        mypage = UserAndCommunityModel.objects.all()
        serializer = CommunitySerializerForMyPage(mypage, many=True)
        return Response(serializer.data)
