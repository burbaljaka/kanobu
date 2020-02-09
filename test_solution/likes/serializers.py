from rest_framework import serializers
from .models import Post

class PostViewSerializer(serializers.ModelSerializer):
    marks = serializers.SerializerMethodField('counter')

    class Meta:
        model = Post
        fields = ['id', 'subject', 'body', 'date_published', 'likes', 'dislikes', 'marks']

    def counter(self, obj):
        return obj.likes + obj.dislikes

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'