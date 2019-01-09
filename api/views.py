from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm
# Create your views here.

def home(request):
    return render(request,"api/website.html")

def loginview(request):
    return render(request,"api/login.html")

def processlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Logged in")
        else:
            return HttpResponse("Failed to login")
    else:
        return HttpResponse("Error")

def signup(request):
    
    return render(request,"api/signup.html")

def register(request):
    if request.method == 'POST':
              
      form = SignUpForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(username=username, password=raw_password)
          login(request,user)
          return redirect("Register")

      else:
       form=SignUpForm()
       return HttpResponse (request, 'api/signup.html',{'form': form}) 
