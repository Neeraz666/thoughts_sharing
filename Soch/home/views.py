from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import *

# Create your views here.
@login_required
def home(request):
    user = request.user
    return render(request, 'home/index.html', {'user': user})