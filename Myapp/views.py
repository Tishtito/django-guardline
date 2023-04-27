from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
from Myapp.models import Student
from Myapp.forms import StudentForm,Employeeform


# Create your views here.
def hello(request):
    return HttpResponse("Welcome to Django")

def hi(request):
    return HttpResponse("Hello there,Glory")

def sup(request):
    return  HttpResponse("Sup my G")

def hey(request):
    return HttpResponse("Hey!")

def evenodd(request):
    x = 28
    if x%2==0:
        return HttpResponse("Number is even")
    else:
        return HttpResponse("Number is odd")

def error(request):
    x=20
    if x==30:
        return HttpResponse("Page found")
    else:
        return HttpResponseNotFound("Page not found")

def index(request):
    return render(request, 'Myapp/index.html')

def variables(request):
    details={
        "Firstname":"Tito",
        "Lastname":"Frank",
        "age":18
    }
    return render(request, 'Myapp/variables.html', details)


def employee(request):
    return render(request, 'Myapp/employee.html')

def image(request):
    return render(request, 'Myapp/images.html')

def background(request):
    return render(request, 'Myapp/backgroundimage.html')

def members(request):
    all = Student.objects.all()
    return render(request, 'Myapp/members.html', {'members':all})

def student(request):
    if request.method=='post':
        form=StudentForm(request.post)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form=StudentForm()
        return render(request, 'Myapp/students.html', {'form':form})

def employee2(request):
    emp= Employeeform()
    return render(request, 'Myapp/employee2.html', {'form':emp})

def setsession(request):
    request.session['firstname']='Frankline'
    request.session['lastname']='eMobilis'
    request.session['email']='tishtito01@gmail.com'
    return HttpResponse("Session has been successfully created")

def getsession(request):
    fname=request.session['firstname']
    lname=request.session['lastname']
    email=request.session['email']
    return HttpResponse(fname+' '+lname+' '+email)

def form(request):
    return render(request, 'Myapp/form.html')

def form2(request):
    return render(request, 'Myapp/form2.html')