from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Add this import
from .forms import CustomUserCreationForm  # Fix the typo here (was .forms)
from devices.models import Device  # Add this import

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Register view
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created! You can now log in.")
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Dashboard view
@login_required
def dashboard_view(request):
    # Add this line to get the user's devices
    devices = request.user.device_set.all()
    return render(request, 'users/dashboard.html', {'devices': devices})

# Profile view
@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

# Logout view
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')

# Home view
def home_view(request):
    return render(request, 'users/home.html')