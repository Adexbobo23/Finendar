from django.urls import path
from .views import (
    participant_dashboard, myprofile, myquize, assignment,
    courses, wishlist, student_settings, student_message,
    reviews, product_wishlist, remove_from_wishlist,
    remove_from_course_wishlist
)

urlpatterns = [
    path('dashboard/', participant_dashboard, name='participant-dashboard'),
    path('my-profile/', myprofile, name='my-profile'),
    path('my-quiz/', myquize, name='my-quiz'),
    path('my-assignment/', assignment, name='student-assignment'),
    path('my-courses/', courses, name='my-course'),
    path('wishlist/', wishlist, name='my-wishlist'),
    path('product-wishlist/', product_wishlist, name='my-product-wishlist'),
    path('my-settings/', student_settings, name='student-settings'),
    path('my-messages/', student_message, name='student-message'),
    path('my-reviews/', reviews, name='student-reviews'),
    path('remove_from_wishlist/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('remove_from_course_wishlist/<int:course_id>/', remove_from_course_wishlist, name='remove_from_course_wishlist'),
]