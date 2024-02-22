from django.urls import path
from .views import (
    instructors_dashboard,
    my_profile,
    message,
    wishlist,
    reviews,
    my_quiz_attempts,
    order_history,
    my_course,
    announcements,
    quiz_attempt,
    assignments,
    instructor_settings,
    instructor_details
)

urlpatterns = [
    path('instructors-dashboard/', instructors_dashboard, name='instructors_dashboard'),
    path('my-profile/', my_profile, name='instructors_my_profile'),
    path('message/', message, name='instructors_message'),
    path('wishlist/', wishlist, name='instructors_wishlist'),
    path('reviews/', reviews, name='instructors_reviews'),
    path('my-quiz-attempts/', my_quiz_attempts, name='instructors_my_quiz_attempts'),
    path('order-history/', order_history, name='instructors_order_history'),
    path('my-course/', my_course, name='instructors_my_course'),
    path('announcements/', announcements, name='instructors_announcements'),
    path('quiz-attempt/', quiz_attempt, name='instructors_quiz_attempt'),
    path('assignments/', assignments, name='instructors_assignments'),
    path('settings/', instructor_settings, name='instructors_settings'),
    path('instructor/<int:instructor_id>/', instructor_details, name='instructor_details'),
]
