from django.db import models
from community.models import Community as CommunityModel
from user.models import CustomUser as CustomUserModel

# Create your models here.
class Noticeboard(models.Model):
    community = models.ForeignKey(CommunityModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    is_public = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class UserAndNoticeboard(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    noticeboard = models.ForeignKey(Noticeboard, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
