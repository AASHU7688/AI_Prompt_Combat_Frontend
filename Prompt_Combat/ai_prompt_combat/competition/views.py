from django.shortcuts import render

# Create your views here.
import openai
import cv2
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def compition_page(request):
    return render(request, 'compition_page.html')

# Leaderboard view
def leaderboard(request):
    submissions = Submission.objects.all().order_by('-total_score')
    return render(request, 'leaderboard.html', {'submissions': submissions})
def home(request):
    return render(request, 'home.html')

def rules(request):
    return render(request, 'rules.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # Create User
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        # Store signup details
        signup_data = Signup(user=user, name=name, gender=gender, mobile=mobile, email=email, password=password)
        signup_data.save()

        messages.success(request, "Signup successful! You can now log in.")
        return redirect('login')

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
    
    return render(request, "login.html")

from django.shortcuts import render

def level1(request):
    message = ""
    if request.method == "POST":
        prompt_text = request.POST.get("prompt_text")  # Get input from the form
        print("Level 1 Submitted Prompt:", prompt_text)  # Debugging output
        message = "Prompt submitted successfully!"

    return render(request, "level1.html", {"message": message})

def level2(request):
    message = ""
    if request.method == "POST":
        reference_image = request.FILES.get("reference_image")  # Get uploaded file
        print("Level 2 Submitted Image:", reference_image)  # Debugging output
        message = "Image submitted successfully!"

    return render(request, "level2.html", {"message": message})

def leaderboard(request):
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})