from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views
from django.urls import re_path

router = DefaultRouter()
router.register("blogs", views.PostModelViewSet)

urlpatterns = [
     path("", include(router.urls)),
	re_path('login', views.login),
	re_path('signup', views.signup),
	re_path('test_token', views.test_token),
]

# get_recent_blogs = http://127.0.0.1:8008/blogs/recent
# sepecific_blog = http://127.0.0.1:8008/blogs/:slug