from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('add/', add, name="addPost")
]