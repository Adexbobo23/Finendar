from django.shortcuts import render
from courses.models import Course

# Create your views here.
def home(request):
    courses = Course.objects.all()[:10]
    context = {
        'courses': courses
    }
    return render(request, 'index.html', context)


def about(request):
    courses = Course.objects.all()[:10]
    context = {
        'courses': courses
    }
    return render(request, 'about.html', context)