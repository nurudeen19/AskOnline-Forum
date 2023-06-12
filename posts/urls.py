from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create', views.create, name='post.create'),
    path('post/<slug:slug>', views.show, name='post.show'),
    path('post/<slug:slug>/comment', views.comment, name='post.comment'),
    path('post/<slug:slug>/delete-comment/<comment_id>', views.delete_comment, name='post.comment.delete'),
]