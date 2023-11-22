from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    # return HttpResponse('This is the homepage')

    context = {'first_name': "John Doe"}

    return render(request, 'crm/index.html', context)


def register(request):
    # return HttpResponse('This is the reg page')
    return render(request, 'crm/register.html')
