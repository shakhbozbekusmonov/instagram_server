from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, \
    PostCommentListView, PostCommentCreateView, CommentListCreateApiView, PostLikeListView, \
    CommentRetrieveView, CommentLikeListView, PostLikeApiView, CommentLikeAPiView

urlpatterns = [
    path('list/', PostListApiView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post_retrieve'),
    path('<uuid:pk>/likes/', PostLikeListView.as_view(), name='post_like_list'),
    path('<uuid:pk>/comments/', PostCommentListView.as_view(), name='post_comment_list'),
    path('<uuid:pk>/comments/create/', PostCommentCreateView.as_view(), name='post_comment_create'),

    path('comments/', CommentListCreateApiView.as_view(), name='comment_list'),
    path('comments/<uuid:pk>/', CommentRetrieveView.as_view(), name='comment_retrieve'),
    path('comments/<uuid:pk>/likes/', CommentLikeListView.as_view(), name='comment_like_list'),

    path('<uuid:pk>/create-delete-like/', PostLikeApiView.as_view(), name='delete_like'),
    path('comments/<uuid:pk>/create-delete-like/', CommentLikeAPiView.as_view(), name='comment_like_create'),
]
