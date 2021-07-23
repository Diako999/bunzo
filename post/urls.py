from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('write_post/', views.write_post, name = 'write_post'),
    path('publish/', views.publish_post, name= 'publish'),
    path('<int:id>', views.post_detail, name= 'post_detail'),
]
