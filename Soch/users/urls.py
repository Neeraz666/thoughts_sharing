from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='signup'),
    path('signup', views.signuppage, name='signup')
]