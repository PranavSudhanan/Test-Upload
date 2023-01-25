from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            add = a.cleaned_data['address']
            gen = a.cleaned_data['gender']
            stat = a.cleaned_data['state']
            b = regmodel(name=nm, address=add, gender=gen, state=stat)
            b.save()
            return HttpResponse('Registered')
        else:
            return HttpResponse('Failed')
    else:
        return render(request, 'register.html')


