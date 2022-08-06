from . import views
from django.urls import path
from .views import BlogPostLike


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>', views.BlogPostDetailView.as_view(), name='user_post_detail'),
    path('<int:pk>', views.BlogPostLike, name="blogpost_like"),
]