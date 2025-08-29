from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'email', 'password', 'phone']



        class UserCreateSerializer(BaseUserCreateSerializer):
            class Meta(BaseUserCreateSerializer.Meta):
                fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone']

        class CreateInviteSerializer(serializers.Serializer):
            first_name = serializers.CharField(max_length=255, allow_blank=False)
            last_name = serializers.CharField(max_length=255, allow_blank=False)
            phone = serializers.CharField(max_length=11, min_length=11, allow_blank=False)
            expires_at = serializers.DateTimeField()