

from django.forms import ModelForm
from django import forms

from django.forms.widgets import PasswordInput, TextInput

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from . models import Task



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password1']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



