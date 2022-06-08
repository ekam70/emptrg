from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from rest_framework import viewsets

from training.models import Department, Cadre, EmployeeStatus, ProgramType, Program, Employee, Detail
from training.forms import EmployeeProgramForm
from training.serializers import EmployeeSerializer

def index(request):
    num_departments = Department.objects.count()
    num_programs = Program.objects.count()
    num_employees = Employee.objects.count()
    num_regular_employees = Employee.objects.filter(status__exact=1).count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    context = {
        'num_departments': num_departments,
        'num_programs': num_programs,
        'num_employees': num_employees,
        'num_regular_employees': num_regular_employees,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class EmployeeListView(generic.ListView):
    model = Employee
    paginate_by = 20


class EmployeeDetailView(generic.DetailView):
    model = Employee


class DepartmentListView(generic.ListView):
    model = Department
    paginate_by = 20


class DepartmentDetailView(generic.DetailView):
    model = Department


def EmployeeProgramNominate(request, employeepsnumber, programcode):
    emp = Employee.objects.get(pk=employeepsnumber)
    prog = Program.objects.get(pk=programcode)
    det = Detail.objects.filter(employee=employeepsnumber, program=programcode)

    return render(request, 'training/employee_program_detail.html', context={'employee': emp, 'program': prog, 'detail': det})


def EmployeeProgramList(request):
    emp = Employee.objects.all()
    prog = Program.objects.all()
    context = {
        'employeelist': emp,
        'programlist': prog,
        'form': EmployeeProgramForm}
    return render(request, 'training/employee_program_list.html', context)


def EmployeeListJson(request):
    emplist=Employee.objects.all()
    emplistjson = []
    for emp in emplist:
        emplistjson.append(emp.getjson())

    return JsonResponse(emplistjson, safe=False)

def ProgramListJson(request):
    proglist=Program.objects.all()
    proglistjson = []
    for prog in proglist:
        proglistjson.append(prog.getjson())

    return JsonResponse(proglistjson, safe=False)


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

