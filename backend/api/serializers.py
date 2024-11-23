from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ["id", "title", "content", "slug"]

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']


# class JoinSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Join 
#         fields = ["id", "title", "firstName", "lastName", "password", "email", "confirmEmail", "city", "country", "slug"]


# get_recent_blogs = http://127.0.0.1:8000/blogs/recent
# sepecific_blog = http://127.0.0.1:8000/blogs/:slug