from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from article.serializers import UserCreateSerializer


# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        return Response({
            "message": "User created successfully",
            "user": UserCreateSerializer(user).data
        } , status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # class CommentSerializer(serializers.ModelSerializer):
    #     user = serializers.StringRelatedField(read_only=True)
    #
    #     class Meta:
    #         model = Comment
    #         fields = ['id', 'content', 'created_at', 'user', 'post']
    #
    # # Like Serializer
    # class LikeSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Like
    #         fields = ['id', 'type', 'user', 'post']
    #
    # # Repost Serializer
    # class RepostSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Repost
    #         fields = ['id', 'user', 'post', 'created_at']
