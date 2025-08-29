from django.urls import path, include
from . import views

url_patterns = [
    path('register', include(views.register_user))
]