from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from community.serializers import CommunitySerializer, UserAndCommunitySerializer

from community.models import Community as CommunityModel
from community.models import UserAndCommunity as UserAndCommunityModel
# Create your views here.
class MainLoginedCommunity(APIView):
    def get(self, request):
        user = request.user
        if user.is_anonymous:
            public_community = CommunityModel.objects.filter(is_public=True)
            serializer = CommunitySerializer(public_community, many=True)
            return Response(serializer.data)
        
        user_community = UserAndCommunityModel.objects.filter(user = request.user)
        user_community_serializer = UserAndCommunitySerializer(user_community, many=True)      
        return Response(user_community_serializer.data)