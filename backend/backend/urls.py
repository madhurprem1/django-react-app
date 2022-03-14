from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('about/', include('blog.urls')),
    path('contact/', include('contact_form.urls')),
    #user register and login
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]
