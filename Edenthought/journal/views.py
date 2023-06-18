


from django.shortcuts import render, redirect
from django.http import HttpResponse

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages   


# Home Page ------------------------------------------------------
def home(request):
    return render(request, 'index.html')


# Register -------------------------------------------------------
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created!")
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'register.html', context)


# Login -------------------------------------------------------
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form':form}
    return render(request, 'my-login.html', context)




# Dashboard ---------------------------------------------------
@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'dashboard.html')
    


# Logout ---------------------------------------------------
@login_required
def user_logout(request):
    auth.logout(request)
    return redirect('my-login')
