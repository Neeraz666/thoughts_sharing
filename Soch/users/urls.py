from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginpage, name="login"),
    path("signup/", views.signuppage, name="signup"),
    path("handlesignup", views.handlesignup, name="handlesignup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('handlelogout', views.handlelogout, name="handlelogout"),
]
