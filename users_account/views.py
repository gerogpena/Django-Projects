from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CreateSignUpForm, ChangePasswordForm

# Create your views here.

def signup_user(request):
    form = CreateSignUpForm()
    
    if request.method =="POST":
        form = CreateSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    
    context ={
        "form":form
    }
    return render(request, "users/signup.html", context)

def login_user(request):

    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember', False) 

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if not remember_me:
                # Set session expiry to default (using SESSION_COOKIE_AGE)
                request.session.set_expiry(0)
                
            return redirect('home')
        else:
            messages.info(request, ("There was an error logging in. Please try again!"))
            return redirect('users:login')
    else:
        return render(request, "users/login.html",{})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout successfully!"))
    return redirect('home')

def user_profile(request):
    user = User.objects.get(username=request.user)

    context = {

        'user':user
    }

    return render (request, "users/user_profile.html", context)

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('user_dashboard')  # Redirect to the settings page or a success page
    else:
        form = ChangePasswordForm(request.user)
        
    return render(request, 'users/change_password.html', {'form': form})