from django.shortcuts import render
from .models import *

# Create your views here.
def loginpage(request):
    return render(request, 'User/login.html')

def signuppage(request):
    return render(request, 'User/signup.html')

def handlelogin(request):
    pass

def handlesignup(request):
    if request.method=="POST":
        email = request.POST('email')
        username = request.POST('username')
        first_name = request.POST('first_name')
        last_name = request.POST('last_name')
        password1 = request.POST('password1')
        password2 = request.POST('password2')
        profile_pic = request.POST('profile_pic')
        gender = request.POST('gender')
        dob = request.POST('dob')
        phone = request.POST('phone')
        address = request.POST('address')
