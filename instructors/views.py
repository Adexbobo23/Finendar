from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InstructorForm


@login_required(login_url='login')
def instructors_dashboard(request):
    return render(request, 'dashboard/instructor-dashboard.html')


@login_required(login_url='login')
def my_profile(request):
    return render(request, 'dashboard/instructor-profile.html')


@login_required(login_url='login')
def message(request):
    return render(request, 'dashboard/instructor-message.html')


@login_required(login_url='login')
def wishlist(request):
    return render(request, 'dashboard/instructor-wishlist.html')


@login_required(login_url='login')
def reviews(request):
    return render(request, 'dashboard/instructor-reviews.html')


@login_required(login_url='login')
def my_quiz_attempts(request):
    return render(request, 'dashboard/instructor-quiz-attempts.html')


@login_required(login_url='login')
def order_history(request):
    return render(request, 'dashboard/instructor-order-history.html')


@login_required(login_url='login')
def my_course(request):
    return render(request, 'dashboard/instructor-course.html')


@login_required(login_url='login')
def announcements(request):
    return render(request, 'dashboard/instructor-announcments.html')


@login_required(login_url='login')
def quiz_attempt(request):
    return render(request, 'dashboard/instructor-quiz-attempts.html')


@login_required(login_url='login')
def assignments(request):
    return render(request, 'dashboard/instructor-assignments.html')


@login_required(login_url='login')
def settings(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the Instructor model
            instructor_profile = form.save(commit=False)
            instructor_profile.user = request.user  
            instructor_profile.save()
            return redirect('instructors_my_profile')
    else:
        form = InstructorForm(instance=request.user.instructor)
    return render(request, 'dashboard/instructor-settings.html')