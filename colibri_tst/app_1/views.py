from django.shortcuts import render, redirect
from app_1.models import Employee
from app_1.forms import FormEmployee
# from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    if request.method=="GET":
        try:
            id=request.GET["id"]
            Employee.objects.get(id=id).delete()
            return redirect(request, "app_1/index.html")
        except:            
            emp_all = Employee.objects.all()
            nr = emp_all.count()
            return render(request, "app_1/index.html", {"cntx":{"emp_all":emp_all, "nr_on_pg":nr}})
        
    if request.method=="POST":
        print(request.POST["id"])
        update(request)

def add_employee(request):    
    form = FormEmployee()
    if request.method == "POST":
        form = FormEmployee(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(request.POST) 

    return render(request, "app_1/add_employee.html", {"form":form})

def update(request):
    if request.method == "POST":        
        form = FormEmployee(request.POST)       
        if form.is_valid():
            form.save(commit=True)
            emp_all = Employee.objects.all()
            nr = emp_all.count()
            return render(request, "app_1/index.html")
        else:
            print(request.POST)

def relative_path(request):
    return render(request, "app_1/relative_path.html")
