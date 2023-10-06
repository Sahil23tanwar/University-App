from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login
from student.models import *
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def courses(request):
    return render(request,"courses.html")

def admission(request):
    return render(request,"admission.html")

def login1(request):
       if request.method=="POST":
           username=request.POST['username']  
           password=request.POST['password']  
           user = auth.authenticate(username=username, password=password)
           if user is not None:
                auth.login(request, user)
                print('logged in')
                return render(request,"addstudents.html")
       else:
         return render(request,"login1.html")
       
def addstudents(request):
        if request.method=="POST":
               student_id=request.POST.get('student_id')
               sname=request.POST.get('sname')
               marks=request.POST.get('marks')
               course=request.POST.get('course')
               s=student(student_id=student_id,sname=sname,marks=marks,course=course);
               s.save();
        return render(request,"addstudents.html");

def editstudents(request):
    studs=student.objects.all();
    return render(request,"editstudents.html",{'studs':studs})

def deletestudents(request,student_id):
       std=student.objects.get(pk=student_id);
       std.delete();
       return render(request,"addstudents.html") 

def updatestudents(request,student_id):
       prd=student.objects.get(pk=student_id);
       return render(request,"addstudents.html",{'prd':prd})

def viewstudents(request):
       studs=student.objects.all();
       return render(request,"viewstudents.html",{'studs':studs})

def logout1(request):
    if request.method=="POST":
         logout(request)
         print('logged out');
         return redirect('about')
    return HttpResponse('logout failed')