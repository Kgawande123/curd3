from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person

# Create your views here.
def pview(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Save DATA")
    return render(request,"app1/person.html",{"form":form})

def hview(request):
    return render(request,"app1/home.html",{})


def sview(request):
    per = Person.objects.all()
    print(per)

    return render(request,"app1/show.html",{"obj":per})


def uview(request,pk):
    obj = Person.objects.get(pid=pk)
    print(obj)
    form = PersonForm(instance=obj)
    if request.method == "POST":
        form = PersonForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/person.html",{"form":form})

def dview(request,x):
    obj = Person.objects.get(pid=x)
    if request.method=="POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/sucess.html",{"obj":obj})
