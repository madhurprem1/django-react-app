from django.urls import path

from . import views


app_name = 'contact_form'

urlpatterns = [
    path('us/', views.ContactFormView.as_view(), name='contact'),
]