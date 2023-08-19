from django.http import HttpResponse
from django.shortcuts import render
from tabledata.models import insertdata

def home(request):
    return render(request,"index.html")

def insert(request):
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            phone=request.POST.get('phone')
            city=request.POST.get('city')    
            data=insertdata(name=name,phone=phone,city=city)
            data.save()
    except:
        pass

    return render(request,"insert.html")

def viewall(request):
    all_data=insertdata.objects.all()
    data={
        'da':all_data
    }
    return render(request,"viewall.html",data)

def deleteupdate(request):
    return render(request,"delete.html")

def help(request):
    return render(request,"help.html")