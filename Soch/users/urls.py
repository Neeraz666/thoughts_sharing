from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginpage, name="login"),
    path("signup/", views.signuppage, name="signup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path("handlesignup", views.handlesignup, name="handlesignup"),
]
