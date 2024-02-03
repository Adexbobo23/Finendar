from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def participant_dashboard(request):
    return render(request, 'dashboard/student-dashboard.html')

@login_required(login_url='login')
def myprofile(request):
    return render(request, 'dashboard/student-profile.html')

@login_required(login_url='login')
def student_message(request):
    return render(request, 'dashboard/student-message.html')

@login_required(login_url='login')
def courses(request):
    return render(request, 'dashboard/student-enrolled-courses.html')

@login_required(login_url='login')
def wishlist(request):
    return render(request, 'dashboard/student-wishlist.html')

@login_required(login_url='login')
def reviews(request):
    return render(request, 'dashboard/student-reviews.html')

@login_required(login_url='login')
def myquize(request):
    return render(request, 'dashboard/student-my-quiz-attempts.html')

@login_required(login_url='login')
def assignment(request):
    return render(request, 'dashboard/student-assignments.html')

@login_required(login_url='login')
def student_settings(request):
    return render(request, 'dashboard/student-settings.html')
