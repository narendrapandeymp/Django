from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from matplotlib import use
from .models import *

# Create your views here.
def index(request):
    context = {"title": "abc", "firstName": "Satyendra", "lastName": "Pandey"}
    return render(request, "test.html", context)
def login(request):

    userdetails = {
        "satyendra.pandey@sap.com": hash("pass1234"),
        "test@test.com": hash("test")
    }

    if request.method == "POST":
        user = User(request.POST)
        user.save()
    else:
        return render(request, "login.html")
def about(request):
    return HttpResponse("its jjjjjjjjjjjjjjjjnot my style")
def ok(request):
    return HttpResponse("its oooooooooooooooonot my style")  
def px(request):
    return HttpResponse("its ppppppppppppppppppnot my style")   