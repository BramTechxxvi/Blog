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

        # from rest_framework.decorators import api_view, permission_classes
        # from rest_framework.permissions import IsAuthenticated
        # from rest_framework.response import Response
        # from rest_framework import status
        # from django.shortcuts import get_object_or_404
        # from .models import Post, Comment, Like, Repost
        # from .serializers import PostSerializer, CommentSerializer, LikeSerializer, RepostSerializer
        # from rest_framework.response import Response
        # from rest_framework import status
        # from .serializers import UserCreateSerializer

        @api_view(['POST'])
        @permission_classes([AllowAny])  # Anyone can register
        def register_user(request):
            serializer = UserCreateSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    "message": "User registered successfully",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "phone": user.phone,
                    }
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # --- POSTS ---
        # @api_view(['GET', 'POST'])
        # @permission_classes([IsAuthenticated])
        # def posts(request):
        #     if request.method == 'GET':
        #         posts = Post.objects.all().order_by('-created_at')
        #         serializer = PostSerializer(posts, many=True)
        #         return Response(serializer.data)
        #
        #     if request.method == 'POST':
        #         serializer = PostSerializer(data=request.data)
        #         serializer.is_valid(raise_exception=True)
        #         serializer.save(user=request.user)
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)

        # --- COMMENTS ---
        # @api_view(['POST'])
        # @permission_classes([IsAuthenticated])
        # def add_comment(request, post_id):
        #     post = get_object_or_404(Post, id=post_id)
        #     serializer = CommentSerializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save(user=request.user, post=post)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        # --- LIKES ---
        # @api_view(['POST'])
        # @permission_classes([IsAuthenticated])
        # def add_like(request, post_id):
        #     post = get_object_or_404(Post, id=post_id)
        #     serializer = LikeSerializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save(user=request.user, post=post)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        # --- REPOSTS ---
        # @api_view(['POST'])
        # @permission_classes([IsAuthenticated])
        # def repost(request, post_id):
        #     post = get_object_or_404(Post, id=post_id)
        #     serializer = RepostSerializer(data={'post': post.id})
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save(user=request.user, post=post)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)


