from django.shortcuts import render, redirect
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
