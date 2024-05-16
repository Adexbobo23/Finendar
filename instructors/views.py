from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import InstructorForm
from .models import Instructor


@login_required(login_url='login')
def instructors_dashboard(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-dashboard.html', {'instructor_profile': instructor_profile})

def instructor_details(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    return render(request, 'instructor-details.html', {'instructor': instructor})
    
@login_required(login_url='login')
def my_profile(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-profile.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def message(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-message.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def wishlist(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-wishlist.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def reviews(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-reviews.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def my_quiz_attempts(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-quiz-attempts.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def order_history(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-order-history.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def my_course(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-course.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def announcements(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-announcments.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def quiz_attempt(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-quiz-attempts.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def assignments(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None
    return render(request, 'dashboard/instructor-assignments.html', {'instructor_profile': instructor_profile})


@login_required(login_url='login')
def instructor_settings(request):
    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        instructor_profile = None

    try:
        instructor_profile = Instructor.objects.get(user=request.user)
    except ObjectDoesNotExist:
        instructor_profile = None

    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES, instance=instructor_profile)
        if form.is_valid():
            # Save the form data to the Instructor model
            instructor_profile = form.save(commit=False)
            instructor_profile.user = request.user
            instructor_profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('instructors_my_profile')
        else:
            print(form.errors)
            messages.error(request, "Error updating profile. Please check the form.")
    else:
        form = InstructorForm(instance=instructor_profile)

    return render(request, 'dashboard/instructor-settings.html', {'form': form, 'instructor_profile': instructor_profile})