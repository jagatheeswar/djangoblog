from django.urls import path

from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, UserFilterView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-jaga'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('filter/dummy', views.filter, name='filter'),
    path('search/dummy', views.search, name='search'),
    path('comment/', views.Realcomment, name='comment'),
    path('commentsection/', views.Realcommentsection, name = 'commentsection'),
    path('like/<int:pk>', views.Likeview, name = 'like_post')
]