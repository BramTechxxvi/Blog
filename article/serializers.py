from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import User

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['username', 'email', 'password', 'phone']
        extra_kwargs = {
            'password': {'write_only': True},
        }

class PostSerializer(serializers.ModelSerializer):