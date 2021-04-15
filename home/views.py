from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is hompage")
def loginuser(request):
    if request.method =="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # return render(request, 'index.html')
    # A backend authenticated the credentials
    # return redirect('home')
    else:
        return render(request, 'login.html')
        # return redirect('/login')
        
def logoutuser(request):
        logout(request)
        return redirect('/login')

def about(request):
    return render(request, 'about.html')

def services(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, 'services.html')
def contact(request):
    if request.method =="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        contact =  Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save();
    messages.success(request, 'Message send successfully')

    return render(request, 'contact.html')