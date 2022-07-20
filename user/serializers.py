from user.models import CustomUser as CustomUserModel
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['user_id', 'password', 'username']
        
        extra_kwarge = {
            'password':{'write_only':True},
            'user_id':{
                'required': '아이디를 작성해주세요',
                'invalid': '이미 존재하는 아이디입니다'
            },
            'username':{
                'required': '이름을 작성해주세요'
            }
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
        
class CustomUserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id
        token['username'] = user.username
        token['user_id'] = user.user_id
        return token