# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm

def register_view(request):
    """Register a new user and log them in."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("blog:index")  # change target as needed
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


def login_view(request):
    """Log a user in."""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect("blog:index")  # change target as needed
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})


def logout_view(request):
    """Log the user out."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "blog/logout.html")


@login_required
def profile_view(request):
    """View and edit user profile (username & email)."""
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("blog:profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})
