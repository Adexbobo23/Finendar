from django.urls import path
from . import views

urlpatterns = [
    path('create_survey/', views.create_survey, name='create_survey'),
    path('create_question/<int:survey_id>/', views.create_question, name='create_question'),
    path('survey_detail/<int:survey_id>/', views.survey_detail, name='survey_detail'),
    path('all/', views.survey_list, name='survey_list'),
    path('survey/<int:survey_id>/', views.survey_question_detail, name='survey_questions_detail'),
]
