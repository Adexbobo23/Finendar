from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import CompanyProfile, Project
from .forms import CompanyProfileForm
from django.contrib import messages
from .forms import ProjectForm

# ProjectViews
@login_required(login_url='login')
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user  
            project.save()
            form.save_m2m() 
            return redirect('project_list')  
    else:
        form = ProjectForm()
    return render(request, 'dashboard/create-project.html', {'form': form})

@login_required(login_url='login')
def project_list(request):
    projects = Project.objects.filter(creator=request.user)
    return render(request, 'dashboard/project_list.html', {'projects': projects})

@login_required(login_url='login')
def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'dashboard/project_details.html', {'project': project})



# Company Views 
@login_required(login_url='login')
def company_admin(request):
    try:
        company_profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        company_profile = None

    return render(request, 'dashboard/admin-dashboard.html', {'company_profile': company_profile})

@login_required(login_url='login')
def company_admin_my_profile(request):
    try:
        company_profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        company_profile = None

    return render(request, 'dashboard/admin-profile.html', {'company_profile': company_profile})

@login_required(login_url='login')
def company_admin_message(request):
    try:
        company_profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        company_profile = None
    return render(request, 'dashboard/admin-message.html')

@login_required(login_url='login')
def company_admin_courses(request):
    try:
        company_profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        company_profile = None

    return render(request, 'dashboard/admin-course.html', {'company_profile': company_profile})

@login_required(login_url='login')
def company_admin_reviews(request):
    try:
        company_profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        company_profile = None

    return render(request, 'dashboard/admin-reviews.html', {'company_profile': company_profile})

@login_required(login_url='login')
def company_admin_quiz_attempts(request):
    try:
        company_profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        company_profile = None

    return render(request, 'dashboard/admin-quiz-attempts.html', {'company_profile': company_profile})


@login_required(login_url='login')
def company_admin_settings(request):
    try:
        company_profile = CompanyProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        company_profile = None

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES, instance=company_profile)
        if form.is_valid():
            # Save the form data to the CompanyProfile model
            company_profile = form.save(commit=False)
            company_profile.user = request.user
            company_profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('company_admin_my_profile')
        else:
            print(form.errors)  
            messages.error(request, "Error updating profile. Please check the form.")
    else:
        form = CompanyProfileForm(instance=company_profile) 

    return render(request, 'dashboard/admin-settings.html', {'form': form, 'company_profile': company_profile})