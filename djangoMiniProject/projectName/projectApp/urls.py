from django.urls import path
from projectApp import views  # Assuming your app is named 'mini'

urlpatterns = [
    path('simple', views.simple_view),
    path('condition', views.check_age),
    path('loop', views.loop),
]