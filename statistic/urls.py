from django.urls import path

from . import views

urlpatterns = [
    path('get/likes/', views.LikeListView.as_view()),
    path('get/user_info/', views.UserRequestInfoView.as_view()),
    ]
