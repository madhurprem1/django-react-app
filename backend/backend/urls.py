from django.contrib import admin
from django.urls import path, include

from login import views
# from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('user/', include('blog.urls')),
    # path('about/', include('blog.urls')),
    #contact_form
    path('contact/', include('contact_form.urls')),
    path("blogpost-like/",include('blog.urls')),
    # path('blogpost-like/<int:pk>', views.BlogPostDetailView, name="blogpost_like"),
    #user register and login
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    path('editor/', include('django_summernote.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)