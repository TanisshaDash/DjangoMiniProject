from django.urls import path

# importing views from views..py
from .views import list_view

urlpatterns = [
    path('', list_view),
]
from django.urls import path

# importing views from views..py
from .views import delete_view
urlpatterns = [
    path('<id>/delete', delete_view ),
]