from django.shortcuts import render
from django.http import HttpResponse

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

