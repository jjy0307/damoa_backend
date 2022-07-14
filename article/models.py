from django.db import models
from noticeboard.models import Noticeboard as NoticeboardModel
from user.models import CustomUser as CustomUserModel
# Create your models here.
class Article(models.Model):
    noticeboard = models.ForeignKey(NoticeboardModel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, null=True, blank=True)
    """user는 on_delete=models.SET_null로 했는데 그 이유는 커뮤니가 사라지면 게시판도 사라지는게 맞지만 유저가 사라져도 글은 기록이 남을수 있기때문입니다.
    """
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/article', null=True)
    file = models.FileField(null=True)
    
class ArticleLikes(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    artcle = models.ForeignKey(Article, on_delete=models.CASCADE)
    likes = models.BooleanField()
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
class CommentLikes(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    likes = models.BooleanField()