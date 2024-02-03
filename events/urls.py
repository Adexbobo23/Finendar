from django.urls import path
from .views import events, zoom_meeting

urlpatterns = [
    path('events/', events, name='event'),
    path('zoom/', zoom_meeting, name="zoom"),
]