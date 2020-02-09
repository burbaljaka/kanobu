from django.urls import path
from .views import ViewPosts,ViewOnePost, MarkPost

urlpatterns = [
    path('allposts/', ViewPosts.as_view()),
    path('allposts/<pk>/', ViewOnePost.as_view()),
    path('allposts/<pk>/<action>/', MarkPost.as_view())
]