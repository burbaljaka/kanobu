from django.urls import path
from .views import ViewPosts,ViewOnePost, SetMark

urlpatterns = [
    path('posts/', ViewPosts.as_view()),
    path('posts/<pk>/', ViewOnePost.as_view()),
    path('<entity>/<pk>/<action>/', SetMark.as_view()),
]