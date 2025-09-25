from django.urls import path
from .views import GeeksFormView, SuccessView

urlpatterns = [
    path('', GeeksFormView.as_view(), name='geeks_form'),
    path('success/', SuccessView.as_view(), name='success'),
]
