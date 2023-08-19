from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def insert(request):
    return render(request,"insert.html")

def viewall(request):
    return render(request,"viewall.html")

def deleteupdate(request):
    return render(request,"delete.html")

def help(request):
    return render(request,"help.html")