from django.urls import path
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create', views.create, name='post.create'),
    path('post/<slug:slug>/edit', views.edit, name='post.edit'),
    path('post/delete/<post_id>', views.delete, name='post.delete'),
    path('post/<slug:slug>', views.show, name='post.show'),
    path('post/<slug:slug>/comment', views.comment, name='post.comment'),
    path('post/<slug:slug>/delete-comment/<comment_id>', views.delete_comment, name='post.comment.delete'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)