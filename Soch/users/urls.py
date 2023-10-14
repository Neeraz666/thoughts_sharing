from django.urls import path
from . import views

urlpatterns = [
    path('loggingin', views.handlelogin, name="handlelogin"),
    path("login/", views.loginpage, name="login"),
    path("signuppage/", views.signuppage, name="signup"),
    path("signup/", views.handlesignup, name="handlesignup"),
]
