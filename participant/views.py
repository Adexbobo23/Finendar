from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from courses.models import EnrolledCourse, Wishlist


@login_required(login_url='login')
def participant_dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = None

    return render(request, 'dashboard/student-dashboard.html', {'user_profile': user_profile})

@login_required(login_url='login')
def myprofile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = None

    return render(request, 'dashboard/student-profile.html', {'user_profile': user_profile})

@login_required(login_url='login')
def student_message(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = None

    return render(request, 'dashboard/student-message.html', {'user_profile': user_profile})

@login_required(login_url='login')
def courses(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = None

    enrolled_courses = EnrolledCourse.objects.filter(user=request.user)
    return render(request, 'dashboard/student-enrolled-courses.html', {'enrolled_courses': enrolled_courses, 'user_profile': user_profile})
    

@login_required(login_url='login')
def wishlist(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = None

    wishlist_items = Wishlist.objects.filter(user=request.user)

    return render(request, 'dashboard/student-wishlist.html', {
        'user_profile': user_profile,
        'wishlist_items': wishlist_items
    })

@login_required(login_url='login')
def reviews(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = None

    return render(request, 'dashboard/student-reviews.html', {'user_profile': user_profile})

@login_required(login_url='login')
def myquize(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = None

    return render(request, 'dashboard/student-my-quiz-attempts.html', {'user_profile': user_profile})

@login_required(login_url='login')
def assignment(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = None
        
    return render(request, 'dashboard/student-assignments.html', {'user_profile': user_profile})
    

@login_required(login_url='login')
def student_settings(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # Save the form data to the UserProfile model
            user_profile = form.save(commit=False)
            user_profile.user = request.user 
            user_profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('my-profile') 
        else:
            print(form.errors)
            messages.error(request, "Error updating profile. Please check the form.")
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'dashboard/student-settings.html', {'form': form, 'user_profile': user_profile})