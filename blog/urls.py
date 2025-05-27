from django.urls import path
from .views import (BlogPageView ,
                    BlogDetailView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView)

urlpatterns = [
    # Home Page
    path('',BlogPageView.as_view(),name='home'),
    # Post Detail Page
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),

    # Create New Post
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    # Edit Post
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    # Delete Post
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
]
