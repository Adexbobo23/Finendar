from django.urls import path
from .views import blog, blog_details

urlpatterns = [
    path('blogs/', blog, name='blog'),
    path('blog/<int:blog_id>/', blog_details, name='blog-details'),
]