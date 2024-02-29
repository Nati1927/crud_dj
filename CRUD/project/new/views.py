from django.shortcuts import render,redirect
from .models import Member
 
# Create your views here.
def index(request):
    mem = Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def add_member(request):
    a = request.POST['first']
    b = request.POST['last']
    c = request.POST['country']
    
    mem=Member(First_name = a, Last_name = b, country = c)
    mem.save()
    
    return redirect("/")

def delete(request,id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem = Member.objects.get(id = id)
    return render(request,'up.html',{'mem':mem})

def upp(request,id):
    a = request.POST['first']
    b = request.POST['last']
    c = request.POST['country']
    mem=Member.objects.get(id=id)
    mem.First_name=a
    mem.Last_name=b
    mem.country=c
    mem.save()
    return redirect("/")