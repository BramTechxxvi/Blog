from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Post, Comment, Like, Repost

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'email','phone', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'phone']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_preview', 'created_at', 'updated_at']

    def content_preview(self, obj):
        return obj.content[:30] + '.....' if len(obj.content) > 30 else obj.content

    content_preview.admin_order_field = 'content'
    content_preview.short_description = 'Content preview'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_preview', 'user', 'post', 'created_at']

    def content_preview(self, obj):
        return obj.content[:30] + '.....' if len(obj.content) > 30 else obj.content

    content_preview.admin_order_field = 'content'
    content_preview.short_description = 'Content preview'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'user', 'post', 'created_at']


@admin.register(Repost)
class RepostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'created_at']

