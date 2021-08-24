from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostupdateView,PostdeleteView,UserPostListView
from . import views
urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),

    path('blog/<int:pk>/',PostDetailView.as_view(),name='blog-detail'),

    path('blog/<int:pk>/update/',PostupdateView.as_view(),name='blog-update'),

    path('blog/<int:pk>/delete/',PostdeleteView.as_view(),name='blog-delete'),

    path('blog/new/',PostCreateView.as_view(),name='blog-create'),
    path('blog/user/<username>',UserPostListView.as_view(), name='blog-user'),
    
    path('about/',views.about, name='blog-about'),
]
