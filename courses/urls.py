from django.urls import path
from .views import (
    create_project, all_courses, 
    course_details, wbt,
    upload_questions, TakeExamView, 
    exam_result, question_upload,
    question_list
    )

urlpatterns = [
    path('create-project/', create_project, name='create-project'),
    path('courses/', all_courses, name='all_courses'),
    path('course/<int:course_id>/', course_details, name='course_details'),
    path('wbt/', wbt, name='wbt'),
    path('upload/', upload_questions, name='upload_questions'),
    path('exam/', TakeExamView.as_view(), name='take_exam'),
    path('result/', exam_result, name='exam_result'),
    path('success/', question_upload, name='question_success'),
    path('questions/', question_list, name='question_list'),
]