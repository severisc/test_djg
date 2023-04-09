from django.shortcuts import render, redirect
from app_1.models import Employee
from app_1.forms import FormEmployee
# from django.http import HttpResponse, HttpResponseRedirect

def chunck_list(chk_sz: int, lst: list) -> list:
    """
    chk_sz: size of chunck
    lst: list that have to split
    return: list of tuple
    """
    out=[]
    m = len(lst)
    lower_bound = 0
    while lower_bound<m-chk_sz:
        out.append((lower_bound, lower_bound+chk_sz))
        lower_bound+=chk_sz
    out.append((lower_bound, m))
    return out

def index(request):
    emp_all = Employee.objects.all()[:20]
    nr = emp_all.count()
    form_empl = []
    for e in emp_all:
        # print(Employee.objects.get(id=e.id))
        form_empl.append(FormEmployee(instance=Employee.objects.get(id=e.id)))

    if request.method=="GET":
        if request.GET.get('id',False):
            id=request.GET["id"]
            Employee.objects.get(id=id).delete()
        return render(request, "app_1/index.html", {"cntx":{"emp_all":emp_all, "nr_on_pg":emp_all.count()}})
    if request.method == "POST":
        emp = Employee.objects.get(id=request.POST["id"])
        form = FormEmployee(request.POST, instance=emp)
        print(form.errors)
        if form.is_valid():
            form.save(commit=True)
        emp_all = Employee.objects.all()[:20]
        nr = emp_all.count()
        form_empl = []
        for e in emp_all:
            form_empl.append(FormEmployee(instance=Employee.objects.get(id=e.id)))
        return render(request, "app_1/index.html", {"cntx":{"emp_all":emp_all, "nr_on_pg":emp_all.count()}})
        
    

def add_employee(request):    
    form = FormEmployee()
    if request.method == "POST":
        form = FormEmployee(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # print(request.POST) 

    return render(request, "app_1/add_employee.html", {"form":form})

def update_emp(request):
    i = request.GET["id"]
    print(f"Id-ul este: {i} !!")
    if i:
        emp = Employee.objects.get(id=request.GET["id"])
    if request.method=="GET":
         form = FormEmployee(instance=emp)
         return render(request, "app_1/update.html", {"form":form})
    else:
        form = FormEmployee(request.POST, instance=emp)
        print("Erori formular", form.errors)
        if form.is_valid():
            form.clean()
            form.save(commit=True)
        emp_all = Employee.objects.all()[:20]
        nr = emp_all.count()
        form_empl = []
        for e in emp_all:
            # print(Employee.objects.get(id=e.id))
            form_empl.append(FormEmployee(instance=Employee.objects.get(id=e.id)))
        return render(request, "app_1/index.html", {"cntx":{"emp_all":emp_all, "nr_on_pg":emp_all.count()}})

def relative_path(request):
    return render(request, "app_1/relative_path.html")
