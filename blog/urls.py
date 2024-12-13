from django.urls import path
from . import views  # Import all views from views.py

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'), 
    path('<int:id>/', views.blog_detail, name='blog_detail'),
    path('<int:id>/delete/', views.blog_delete, name='blog_delete'),
    path('<int:id>/update/', views.blog_update, name='blog_update'),
    path('<int:id>/like/', views.like_post, name='like_post'),
]