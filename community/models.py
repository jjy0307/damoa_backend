from django.db import models
from user.models import CustomUser as CustomUserModel

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)

class Community(models.Model):
    name = models.CharField(max_length=50)
    is_public = models.BooleanField(default=True)
    """
    이미지를 올리시 Django에서 자동적으로 media폴더를 생성해줍니다.
    upload_to를 작성하면 media폴더 안에 폴더를 만들어서 그 안에 이미지가 생성됩니다.
    """
    image = models.ImageField(upload_to="uploads/%Y%m%d", null=True)
    introduction = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"커뮤니티 명: {self.name} / 공개 여부: {self.is_public}"

class TagAndCommunity(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(f'{self.community}의 태그는 {self.tag}입니다.')

class UserAndCommunity(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}의 {self.community} 참여일은 {self.date_joined}입니다. 관리자 여부는 {self.is_admin}입니다."
