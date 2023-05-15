from rest_framework import serializers
from .models import Blog, User, Like

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'blogid', 'blogtitle', 'description', 'Content']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'UserId', 'name', 'email', 'password']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like 
        fields = ['id', 'likeid', 'Userid', 'blogid']
