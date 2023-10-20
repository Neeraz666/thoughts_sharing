from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.
def loginpage(request):
    return render(request, "User/login.html")


def signuppage(request):
    return render(request, "User/signup.html")


def handlelogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Hi {user.username.title()}, welcome back!")
            return redirect("/home")
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect("/login")
    else:   
        return HttpResponse("This view only accepts POST requests.")
    

def handlesignup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        profile_pic = request.FILES.get("profile_pic")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        if len(username) < 6:
            messages.error(request, "Username should be at least 6 letters.")
            return redirect("signup")

        if not username.isalnum():
            messages.error(request, "Username should only contain alphanumerics.")
            return redirect("signup")

        if password1 != password2:
            messages.error(request, "Your passwords dont match. Please try again.")
            return redirect("signup")

        user = User.objects.create_user(email=email, username=username)
        user.first_name = first_name
        user.last_name = last_name
        user.profile_pic = profile_pic
        user.gender = gender
        user.dob = dob
        user.phone = phone
        user.address = address

        user.password = make_password(password1)
        user.save()
        # login(request, user)
        messages.success(request, 'Thank you! Your Soch account has been created, please Login to continue.')
        return redirect("/login")

    else:
        messages.error('Something went wrong. Please fill it carefully.')
        return redirect('signup')


def handlelogout(request):
    logout(request)
    return redirect("/")