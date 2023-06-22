


from django.shortcuts import render, redirect
from django.http import HttpResponse

from . forms import CreateUserForm, LoginForm, ThoughtPostForm, ThoughtUpdateForm, UpdateUserForm, UpdateProfileForm

from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages   

from . models import Thought, Profile  

from django.core.mail import send_mail
from django.conf import settings



# Home Page ------------------------------------------------------
def home(request):
    return render(request, 'index.html')


# Register -------------------------------------------------------
def register(request):
    form = CreateUserForm()
    # form2 = UpdateProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            current_user = form.save(commit=False)
            
            form.save()
            send_mail("Welcome to EdenThought",
                       "Congratulations on creating your account !",
                       settings.DEFAULT_FROM_EMAIL,
                       [current_user.email]) 

            profile = Profile.objects.create(user=current_user)

            messages.success(request, "Your account was created!")
            # return redirect('dashboard')  -- LMC
            return redirect('my-login')
        
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
                messages.success(request, "Login success !")
                return redirect('dashboard')

    context = {'form':form}
    return render(request, 'my-login.html', context)




# Dashboard ---------------------------------------------------
@login_required(login_url='my-login')
def dashboard(request):
    print('*'*20, dir(request))
    print('*'*20, request.user)
    profile_pic = Profile.objects.get(user=request.user)
    context = {'profilePic': profile_pic}

    return render(request, 'profile/dashboard.html', context)
    


# Logout ---------------------------------------------------
@login_required
def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success !")
    return redirect('my-login')



@login_required(login_url='my-login')
def post_thought(request):
    form = ThoughtPostForm()
    if request.method == 'POST':
        form = ThoughtPostForm(request.POST)
        if form.is_valid():
            thought = form.save(commit = False)
            print(thought)
            thought.user = request.user
            thought.save()
            messages.success(request, "You just posted a new thought !")
            return redirect('my-thoughts')

    context = {'form':form}
    return render(request, 'profile/post-thought.html', context)




@login_required(login_url='my-login')
def my_thoughts(request):
    current_user = request.user.id
    my_thoughts = Thought.objects.all().filter(user=current_user)
    context = {'thoughts': my_thoughts}
    return render(request, 'profile/my-thoughts.html', context)




@login_required(login_url='my-login')
def update_thought(request, pk):
    my_thought = Thought.objects.get(id=pk)
    form = ThoughtUpdateForm(instance=my_thought)

    if request.method == 'POST':
        form = ThoughtPostForm(request.POST, instance=my_thought)
        if form.is_valid():
            form.save()
            messages.success(request, "You just updated your thought !")
            return redirect('my-thoughts')

    context = {'form': form}
    return render(request, 'profile/update-thought.html', context)




@login_required(login_url='my-login')
def delete_thought(request, pk):
    my_thought = Thought.objects.get(id=pk)

    if request.method == 'POST':
        my_thought.delete()
        messages.success(request, "You just deleted your thought !")
        return redirect('my-thoughts')
    
    return render(request, 'profile/delete-thought.html')




@login_required(login_url='my-login')
def profile_management(request):
    form = UpdateUserForm(instance=request.user)
    profile = Profile.objects.get(user=request.user)
    form_2 = UpdateProfileForm(instance=profile)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Update - username/email was a success !")
            return redirect('dashboard')
        if form_2.is_valid():
            form_2.save()
            messages.success(request, "Your profile picture was sucessfully updated !")
            return redirect('dashboard')

    context = {'form': form, 'form_2': form_2}
    return render(request, 'profile/profile-management.html', context)



@login_required(login_url='my-login')
def delete_account(request):
    if request.method == 'POST':
        deleteUser = User.objects.get(username=request.user)
        deleteUser.delete()
        messages.success(request, "Your account was sucessfully deleted !")
        return redirect('my-login')
    return render(request, 'profile/delete-account.html')




















