from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from tabledata.models import insertdata
from tabledata.models import helpdata

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
    all_data=insertdata.objects.all()
    data={
        'da':all_data
    }
    return render(request,"delete.html",data)

def deletedata(request,uid):
    get_id=insertdata.objects.get(id=uid)
    get_id.delete()
    url="/deleteupdate/"
    return HttpResponseRedirect(url)

def updatedata(request,uid):
    get_id=insertdata.objects.get(id=uid)
    data={
        'data1':get_id
    }
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            phone=request.POST.get('phone')
            city=request.POST.get('city')    
            datavalue=insertdata(id=uid,name=name,phone=phone,city=city)
            datavalue.save()
            url="/deleteupdate/"
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"update.html",data)

def help(request):
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            phone=request.POST.get('phone')
            city=request.POST.get('msg')    
            data=helpdata(name=name,phone=phone,city=city)
            data.save()
    except:
        pass
    return render(request,"help.html") 