from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def company_admin(request):
    return render(request, 'dashboard/admin-dashboard.html')

@login_required(login_url='login')
def company_admin_my_profile(request):
    return render(request, 'dashboard/admin-profile.html')

@login_required(login_url='login')
def company_admin_message(request):
    return render(request, 'dashboard/admin-message.html')

@login_required(login_url='login')
def company_admin_courses(request):
    return render(request, 'dashboard/admin-course.html')

@login_required(login_url='login')
def company_admin_reviews(request):
    return render(request, 'dashboard/admin-reviews.html')

@login_required(login_url='login')
def company_admin_quiz_attempts(request):
    return render(request, 'dashboard/admin-quiz-attempts.html')

@login_required(login_url='login')
def company_admin_settings(request):
    return render(request, 'dashboard/admin-settings.html')