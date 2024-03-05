from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def create_project(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course_instance = form.save(commit=False)
            course_instance.user = request.user 
            course_instance.save()
            return redirect('instructors_dashboard')
    else:
        form = CourseForm()
    
    return render(request, 'dashboard/create-course.html', {'form': form})


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})


def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Fetch the latest 2 courses
    courses = Course.objects.order_by('-id')[:2]
    context = {
        'course': course,
        'courses': courses
    }
    return render(request, 'course-details.html', context)


def wbt(request):
    return render(request, 'cbt.html')