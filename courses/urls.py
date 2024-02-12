from django.urls import path
from .views import create_project

urlpatterns = [
    path('create-project/', create_project, name='create-project'),
]