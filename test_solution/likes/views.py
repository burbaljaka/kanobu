from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import PostViewSerializer, PostCreateSerializer, CommentSerializer
from .models import Post, Comment
import json

class ViewPosts(generics.ListAPIView):
    serializer_class = PostViewSerializer
    queryset = Post.objects.all()

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid()

        post = Post.objects.create(**serializer.validated_data)
        post.save()

        return Response(PostViewSerializer(post).data)

class ViewOnePost(generics.RetrieveAPIView):
    serializer_class = PostViewSerializer
    queryset = Post.objects.all()

class SetMark(generics.UpdateAPIView):
    def get(self, request, entity=None, pk=None, action=None):
        serializer_class = PostViewSerializer
        if entity == 'posts':
            item = Post.objects.get(pk=pk)
            serializer = PostViewSerializer
        elif entity == 'comments':
            item = Comment.objects.get(pk=pk)
            serializer = CommentSerializer
        return Response(serializer(item).data)

    def post(self, request, entity=None, pk=None, action=None):
        if entity == 'posts':
            item = Post.objects.get(pk=pk)
            serializer = PostViewSerializer
        elif entity == 'comments':
            item = Comment.objects.get(pk=pk)
            serializer = CommentSerializer

        if action == 'like':
            item.likes += 1
        elif action == 'dislike':
            item.dislikes += 1
        else:
            return Response('Received something wrong, please try again')

        item.save()

        result = serializer(item).data
        result['action'] = entity[:-1] + ' received a ' + action

        return Response(result)









