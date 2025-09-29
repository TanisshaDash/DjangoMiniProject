from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mini.urls')),  # <-- make sure this matches your app
]
    