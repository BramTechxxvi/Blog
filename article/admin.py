from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Post, Comment, Like, Repost

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'email','phone', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'phone']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'reduce_content', 'created_at', 'updated_at']

    def reduce_content(self, obj):
        return obj.content[:30] + '.....' if len(obj.content) > 30 else obj.content

    reduce_content.admin_order_field = 'Content preview'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'user', 'post', 'created_at']

    def


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'user', 'post', 'created_at']


@admin.register(Repost)
class RepostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'created_at']

