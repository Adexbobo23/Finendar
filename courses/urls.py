from django.urls import path
from .views import (
    create_project, all_courses, 
    course_details, wbt
    )

urlpatterns = [
    path('create-project/', create_project, name='create-project'),
    path('courses/', all_courses, name='all_courses'),
    path('course/<int:course_id>/', course_details, name='course_details'),
    path('wbt/', wbt, name='wbt'),
]