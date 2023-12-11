from django.urls import path
from .views import *

urlpatterns = [
    path('appointment', appointment, name='appointment'),
    path('delivery', delivery, name='delivery'),
    path('orders', orders, name="orders")
]