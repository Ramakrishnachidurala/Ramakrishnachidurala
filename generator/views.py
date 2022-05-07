import re
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def about(request):
    return render(request,"generator/about.html") 
def home(request):
    return render(request,"generator/home.html")

def sk(request):
    return HttpResponse("<h2>Welcome to sk tutorials</h2>")   

def password(request) :
    password= ""

    characaters= list("abcdefghijklmnopqrstuvwxyz")

    length = int(request.GET.get("length"))

    if request.GET.get("uppercase"):
        characaters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("Specialchar"):
        characaters.extend(list("!@#$%^&*()"))   

    if request.GET.get("Numbers") :
        characaters.extend(list("0123456789"))   



    for x in range(length):
        password +=random.choice(characaters)


    return render(request,"generator/password.html",{"password":password})    

   