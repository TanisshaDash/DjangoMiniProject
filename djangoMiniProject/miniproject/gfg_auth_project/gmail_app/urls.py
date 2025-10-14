from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.gmail_login, name='gmail_login'),
    path('callback/', views.gmail_callback, name='gmail_callback'),
    path('fetch/', views.fetch_emails, name='fetch_emails')
]
