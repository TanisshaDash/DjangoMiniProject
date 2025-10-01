from django.urls import path
from projectApp import views  # Assuming your app is named 'mini'

urlpatterns = [
    path('', views.formset_view, name='home'),

]