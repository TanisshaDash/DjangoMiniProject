from django.contrib import admin
from django.urls import path
from app import views  # <-- change "myapp" to your actual app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_view, name='hello'),
]
