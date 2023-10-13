from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='signup'),
    path('signuppage', views.signuppage, name='signup'),
    path('signup', views.handlesignup, name='handlesignup')
]