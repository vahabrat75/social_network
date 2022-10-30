from django.urls import path, re_path

from . import views

urlpatterns = [
    path('post/create/', views.CreatePost.as_view()),
    path('post/like/', views.LikePost.as_view()),
    ]