from django.urls import path
from .views import (
    create_project, all_courses, 
    course_details, wbt,
    upload_questions, 
    exam_result, question_upload,
    question_list, take_exam,add_to_cart
    )

urlpatterns = [
    path('create-course/', create_project, name='create-project'),
    path('courses/', all_courses, name='all_courses'),
    path('course/<int:course_id>/', course_details, name='course_details'),
    path('wbt/', wbt, name='wbt'),
    path('upload/', upload_questions, name='upload_questions'),
    path('take-exam/<int:question_id>/', take_exam, name='take_exam'),
    path('result/', exam_result, name='exam_result'),
    path('success/', question_upload, name='question_success'),
    path('questions/', question_list, name='question_list'),
    path('add_to_cart/<int:course_id>/', add_to_cart, name='add_to_cart'),
]