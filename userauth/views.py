from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ParticipantRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from participant.models import UserProfile

# All Registration 
def register_participant(request):
    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create UserProfile for the user
            UserProfile.objects.create(user=user)

            login(request, user)
            return redirect('login')
    else:
        form = ParticipantRegistrationForm()
    return render(request, 'register.html', {'form': form})


# All Login
def login_participant(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('participant-dashboard')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_participant(request):
    logout(request)
    return redirect('login')