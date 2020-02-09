from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import PostViewSerializer, PostCreateSerializer
from .models import Post

class ViewPosts(generics.ListAPIView):
    serializer_class = PostViewSerializer
    queryset = Post.objects.all()

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid()

        post = Post.objects.create(**serializer.validated_data)
        post.save()

        return Response(PostViewSerializer(post).data)

class ViewOnePost(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostViewSerializer
    queryset = Post.objects.all()

class MarkPost(generics.UpdateAPIView):
    def get(self, request, pk, action=None):
        serializer_class = PostViewSerializer
        post = Post.objects.get(pk=pk)
        return Response(PostViewSerializer(post).data)

    def post(self, request, pk=None, action=None):
        post = Post.objects.get(pk=pk)
        if action == 'like':
            post.likes += 1
        elif action == 'dislike':
            post.dislikes += 1
        else:
            return Response('Received something wrong, please try again')

        post.save()

        return Response(PostViewSerializer(post).data)







