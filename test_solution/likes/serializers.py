from rest_framework import serializers
from .models import Post

class PostViewSerializer(serializers.ModelSerializer):
    marks = serializers.SerializerMethodField('counter')
    post_type = serializers.SerializerMethodField('type')


    class Meta:
        model = Post
        fields = ['id', 'subject', 'body', 'date_published', 'post_type', 'likes', 'dislikes', 'marks']

    def counter(self, obj):
        return obj.likes + obj.dislikes

    def type(self, obj):
        if obj.post_type == 'n':
            return 'new'
        else:
            return 'post'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'