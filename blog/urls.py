from django.urls import path
from .views import blog

urlpatterns = [
    path('blogs/', blog, name='blog'),
]