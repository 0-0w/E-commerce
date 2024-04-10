from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from .models import SignUp

# Create your views here.
def login(request):
    if request.method == "POST":
        username =    request.POST['name']
        password =    request.POST['pass']

        # user = 
    return render(request , "authentication/login.html") 

def signup(request):
    if request.method == "POST":
        username =    request.POST['name']
        email =       request.POST['email']
        password =    request.POST['pass']
        re_password = request.POST['re_pass']
        signup = SignUp(username = username, email = email, password = password)
        
        if (password != "") and (password == re_password):
            signup.save()
            return redirect("login")
            messages.success(request, "Signed in Successfully, please login now!")

        else:
            if (password == ""):
                messages.error(request, "Please enter password")
            else:
                messages.error(request, "Password does not match")
        
    return render(request , "authentication/signup.html") 

def signout(request):
    pass
