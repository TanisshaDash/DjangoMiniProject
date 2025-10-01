from django.urls import path
from projectApp import views  # Assuming your app is named 'mini'

urlpatterns = [
    path('', views.home_view, name='home'),
]