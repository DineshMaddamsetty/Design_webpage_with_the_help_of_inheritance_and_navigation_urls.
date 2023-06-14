from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')
def dummy(request):
    return render(request,'dummy.html')


# Create your views here.
