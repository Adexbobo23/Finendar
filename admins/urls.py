from django.urls import path
from .views import (
    company_admin,
    company_admin_my_profile,
    company_admin_message,
    company_admin_courses,
    company_admin_reviews,
    company_admin_quiz_attempts,
    company_admin_settings,
    create_project, project_list,
    project_details
)

urlpatterns = [
    path('company-admin/', company_admin, name='company_admin'),
    path('company-admin/my-profile/', company_admin_my_profile, name='company_admin_my_profile'),
    path('company-admin/message/', company_admin_message, name='company_admin_message'),
    path('company-admin/courses/', company_admin_courses, name='company_admin_courses'),
    path('company-admin/reviews/', company_admin_reviews, name='company_admin_reviews'),
    path('company-admin/quiz-attempts/', company_admin_quiz_attempts, name='company_admin_quiz_attempts'),
    path('company-admin/settings/', company_admin_settings, name='company_admin_settings'),
    path('create/', create_project, name='create_project'),
    path('project-list/', project_list, name='project_list'),
    path('project/<int:project_id>/', project_details, name='project_details'),
]
