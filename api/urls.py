from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.viewsPosts),
    path('add/', views.addPosts),
    path('posts/<str:pk>/', views.viewsPostDetail),
    path('update/<str:pk>/', views.updatePosts),
    path('delete/<str:pk>/', views.deletePosts),
]
