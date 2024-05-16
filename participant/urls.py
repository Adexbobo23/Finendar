from django.urls import path
from .views import (
    participant_dashboard, myprofile, myquize, assignment,
    courses, wishlist, student_settings, student_message,
    reviews
)

urlpatterns = [
    path('dashboard/', participant_dashboard, name='participant-dashboard'),
    path('my-profile/', myprofile, name='my-profile'),
    path('my-quiz/', myquize, name='my-quiz'),
    path('my-assignment/', assignment, name='student-assignment'),
    path('my-courses/', courses, name='my-course'),
    path('wishlist/', wishlist, name='my-wishlist'),
    path('my-settings/', student_settings, name='student-settings'),
    path('my-messages/', student_message, name='student-message'),
    path('my-reviews/', reviews, name='student-reviews'),
]