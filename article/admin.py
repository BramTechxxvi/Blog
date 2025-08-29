from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Post
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("id", "content", "user", "post", "created_at")
#     search_fields = ("content",)
#     list_filter = ("created_at",)
#
# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ("id", "type", "user", "post")
#
# @admin.register(Repost)
# class RepostAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "post", "created_at")


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'email','phone', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'phone']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']






# Register your models here.
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", )
#     search_fields = ("title", "content")
#     list_filter = ("created_at",)


