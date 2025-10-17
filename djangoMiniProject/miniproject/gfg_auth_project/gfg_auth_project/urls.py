from django.contrib import admin
from django.urls import path, include
from gmail_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gmail/', include('gmail_app.urls')),
    path('', views.home, name='home'),
]
