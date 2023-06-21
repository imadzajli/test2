from django.shortcuts import render
from django.http import HttpResponse
from sign_up.views import signup

def home(request):
    return render(request,'home.html')

def signup_redirection(request):
    return signup(request)