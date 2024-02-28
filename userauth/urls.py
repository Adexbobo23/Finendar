from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ( 
    login_participant, register_participant,
    logout_participant, activate_account
)

urlpatterns = [
    path('login/', login_participant, name='login'),
    path('logout/', logout_participant, name='logout'),
    path('register/', register_participant, name='register'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
