from django.urls import path
from .views import ( 
    login_participant, register_participant,
    logout_participant 
)

urlpatterns = [
    path('login/', login_participant, name='login'),
    path('logout/', logout_participant, name='logout'),
    path('register/', register_participant, name='register'),
]
