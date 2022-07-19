from django.urls import path, include
from .views import ArticleViewSet, ArticleLikesViewSet, CommentViewSet , CommentLikesViewSet

# 게시글 보기, 작성
article_list = ArticleViewSet.as_view({
    'get':'list',
    'post':'create'
})

# 게시글 수정, 삭제
article_detail = ArticleViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})

# 게시글 추천
article_suggestion = ArticleLikesViewSet.as_view({
    'get':'list',
    'post':'create',
    'put':'update',
    'delete':'destroy',
})

# 댓글 보기, 작성
comment_list = CommentViewSet.as_view({
    'get':'list',
    'post':'create'
})

# 댓글 수정, 삭제
comment_detail = CommentViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})

# 댓글 추천
comment_suggestion = CommentLikesViewSet.as_view({
    'get':'list',
    'post':'create',
    'put':'update',
    'delete':'destroy',
})

urlpatterns = [
    path('article/write/', article_list),
    path('article/write/<int:pk>', article_detail),
    path('article/<int:pk>/suggestion/', article_suggestion),
    path('comment/write/', comment_list),
    path('comment/write/<int:pk>', comment_detail),
    path('comment/<int:pk>/suggestion/', comment_suggestion),
]



