from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    marks = serializers.SerializerMethodField('counter')
    class Meta:
        model = Comment
        fields = ['id', 'author', 'body', 'date_created', 'likes', 'dislikes', 'marks']

    def counter(self, obj):
        return obj.likes + obj.dislikes

class PostViewSerializer(serializers.ModelSerializer):
    marks = serializers.SerializerMethodField('counter')
    post_type = serializers.SerializerMethodField('type')
    comment = serializers.SerializerMethodField('comments')

    class Meta:
        model = Post
        fields = ['id', 'subject', 'body', 'date_published', 'post_type', 'likes', 'dislikes', 'marks', 'comment']

    def counter(self, obj):
        return obj.likes + obj.dislikes

    def type(self, obj):
        if obj.post_type == 'n':
            return 'new'
        else:
            return 'post'

    def comments(self, obj):
        comments = Comment.objects.filter(post=obj.id)
        return CommentSerializer(comments, many=True).data

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'