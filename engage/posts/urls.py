from django.urls import path
from .views import feed
from .views import feed, like_post, add_comment, create_post, delete_post, edit_post

urlpatterns = [
    path('', feed, name='feed'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comment/<int:post_id>/', add_comment, name='add_comment'),
    path('create/', create_post, name='create_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
]