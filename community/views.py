from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class MainLoginedCommunity(APIView):
    def get(self, request):
        print('request', request)
        print('request.user', request.user)
        return Response({'message':'sexypower'})