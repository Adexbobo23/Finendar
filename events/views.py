from django.shortcuts import render

# Create your views here.

def events(request):
    return render(request, 'event-details.html')


def zoom_meeting(request):
    return render(request, 'zoom/zoom-meetings.html')