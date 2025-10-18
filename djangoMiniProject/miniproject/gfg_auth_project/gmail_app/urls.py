from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gmail/login/", views.gmail_login, name="gmail_login"),
    path("gmail/callback/", views.gmail_callback, name="gmail_callback"),
    path("fetch_emails/", views.fetch_emails, name="fetch_emails"),
]
