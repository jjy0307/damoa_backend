from django.db import models
from noticeboard.models import Noticeboard as NoticeboardModel
from user.models import CustomUser as CustomUserModel


class Article(models.Model):
    noticeboard = models.ForeignKey(NoticeboardModel, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUserModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=10000000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, blank=True)
    count = models.PositiveIntegerField(default=0)
    is_valid = models.BooleanField(default=False)


class ArticleAndImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="article/%Y%m%d")


class ArticleLikes(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    artcle = models.ForeignKey(Article, on_delete=models.CASCADE)
    likes = models.BooleanField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUserModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    content = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=False)


class CommentLikes(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    likes = models.BooleanField()

class IpAndArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip = models.CharField(max_length=500)