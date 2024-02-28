from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course
from blog.models import Blog

# Create your views here.
def home(request):
    courses = Course.objects.all()[:10]
    blogs = Blog.objects.all()[:10]
    context = {
        'courses': courses,
        'blogs': blogs
    }
    return render(request, 'index.html', context)


def about(request):
    courses = Course.objects.all()[:10]
    context = {
        'courses': courses
    }
    return render(request, 'about.html', context)