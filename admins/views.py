from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CompanyProfileForm


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
     if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the CompanyProfile model
            company_profile = form.save(commit=False)
            company_profile.user = request.user 
            company_profile.save()
            return redirect('company_admin_my_profile')
    else:
        form = CompanyProfileForm(instance=request.user.companyprofile) 
    return render(request, 'dashboard/admin-settings.html')