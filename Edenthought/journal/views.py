from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from . forms import TaskForm, CreateUserForm, LoginForm

from .models import Task


# Create your views here.



clientList = [
    {
        'id': '1',
        'name': 'Bobby Brown',
        'profession': 'Drawer',
    },{
        'id': '2',
        'name': 'Sarah',
        'profession': 'Carpenter',
    },
]


def register(request):
    return render(request, 'register.html')



def home(request):
    context = {'clients': clientList}
    return render(request, 'index.html',context)



def tasks(request):
    query = Task.objects.all()
    context = {'tasks': query}
    return render(request, 'tasks.html', context)



def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(tasks)

    context = {'form': form}
    return render(request, 'create-task.html', context)



def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(tasks)

    context = {'form': form}
    return render(request, 'update-task.html', context)



def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(tasks)
    return render(request, 'delete-task.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    context = {'form': form}
    return render(request, 'register.html', context)
 


def success(request):
    return render(request, 'success.html')



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
                return redirect("dashboard")

    context = {'form': form}
    return render(request, 'my-login.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def user_logout(request):
    auth.logout(request)
    return redirect('my-login')
















