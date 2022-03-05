from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]