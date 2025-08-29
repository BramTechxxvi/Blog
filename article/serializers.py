from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import User, Post


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['username', 'email', 'password', 'phone']
        extra_kwargs = {
            'password': {'write_only': True},
        }


class PostSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'user']

