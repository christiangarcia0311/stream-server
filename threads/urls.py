from django.urls import path
from .views import (
    ThreadPostListView,
    ThreadPostDetailView,
    UserThreadPostsView,
    ThreadPostCreateView,
    ThreadCommentListCreateView,
    ThreadLikeToggleView,
    ThreadCommentLikeToggleView,
    ThreadCommentReplyListCreateView,
    ThreadCommentReplyLikeToggleView
)

urlpatterns = [
    path('posts/', ThreadPostListView.as_view(), name='thread-list'),
    path('my-posts/', UserThreadPostsView.as_view(), name='user-thread'),
    path('create/', ThreadPostCreateView.as_view(), name='thread-create'),
    path('posts/<int:pk>/', ThreadPostDetailView.as_view(), name='thread-details'),
    path('posts/<int:pk>/comments/', ThreadCommentListCreateView.as_view(), name='thread-comments'),
    path('posts/<int:pk>/like/', ThreadLikeToggleView.as_view(), name='thread-like'),
    path('comments/<int:pk>/like/', ThreadCommentLikeToggleView.as_view(), name='comment-like'),
    path('comments/<int:pk>/replies/', ThreadCommentReplyListCreateView.as_view(), name='comment-replies'),
    path('replies/<int:pk>/like/', ThreadCommentReplyLikeToggleView.as_view(), name='reply-like'),
]
