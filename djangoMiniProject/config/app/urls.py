from django.contrib import admin
from django.urls import path, include
from app import views  # ✅ use your app name here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.hello_view, name='hello'),
]
