# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.urls import reverse

class Department(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'
        ordering = ['code']
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('department-detail', args=[self.code])


    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def getjson(self):
        return {
            'code': self.code,
            'name' : self.name
        }


class Cadre(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadre'

    def __str__(self):
        """String for representing the Model object."""
        return self.description

    def getjson(self):
        return {
            'code': self.code,
            'description' : self.description
        }


class EmployeeStatus(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeestatus'

    def __str__(self):
        """String for representing the Model object."""
        return self.description

    def getjson(self):
        return {
            'code': self.code,
            'description' : self.description
        }


class ProgramType(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programtype'

    def __str__(self):
        """String for representing the Model object."""
        return self.description

    def getjson(self):
        return {
            'code': self.code,
            'description' : self.description
        }


class Program(models.Model):
    code = models.CharField(primary_key=True, max_length=7)
    description = models.CharField(max_length=50, blank=True, null=True)
    minimumeligibility = models.ForeignKey(Cadre, on_delete=models.SET_NULL, db_column='minimumeligibility', blank=True, null=True, related_name='mincadre')
    maximumeligibility = models.ForeignKey(Cadre, on_delete=models.SET_NULL, db_column='maximumeligibility', blank=True, null=True, related_name='maxcadre')
    type = models.ForeignKey(ProgramType, on_delete=models.SET_NULL, db_column='type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program'

    def __str__(self):
        """String for representing the Model object."""
        return self.description

    def getjson(self):
        return {
            'code': self.code,
            'description' : self.description,
            'minimumeligibility' : self.minimumeligibility.getjson(),
            'maximumeligibility' : self.maximumeligibility.getjson(),
            'type' : self.type.getjson()
        }


class Employee(models.Model):
    psnumber = models.IntegerField(primary_key=True)
    initial = models.CharField(max_length=4, blank=True, null=True)
    firstname = models.CharField(max_length=40, blank=True, null=True)
    middlename = models.CharField(max_length=40, blank=True, null=True)
    lastname = models.CharField(max_length=40, blank=True, null=True)
    cadre = models.ForeignKey(Cadre, on_delete=models.SET_NULL, db_column='cadre', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, db_column='department', blank=True, null=True)
    status = models.ForeignKey(EmployeeStatus, on_delete=models.SET_NULL, db_column='status', blank=True, null=True)
    superior = models.ForeignKey('self', on_delete=models.SET_NULL, db_column='superior', blank=True, null=True, related_name='subordinates')

    class Meta:
        managed = False
        db_table = 'employee'
        ordering = ['psnumber']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('employee-detail', args=[str(self.psnumber)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.lastname}, {self.firstname}'

    @property
    def fullname(self):
        return f'{self.lastname}, {self.firstname}'

    @property
    def cadre_code(self):
        return self.cadre.code

    @property
    def department_code(self):
        return self.department.code

    @property
    def status_code(self):
        return self.status.code

    @property
    def superior_psnumber(self):
        return self.superior.psnumber if self.superior else 0

    def superior_info(self):
        return {'psnumber': self.superior.psnumber, 'fullname': self.superior.fullname} if self.superior else {'psnumber': 0, 'fullname': ''}

    def getjson(self):
        return {
            'psnumber': self.psnumber,
            'initial' : self.initial,
            'firstname' : self.firstname,
            'middlename' : self.middlename,
            'lastname' : self.lastname,
            'fullname': self.fullname,
            'cadre' : self.cadre.getjson(),
            'department' : self.department.getjson(),
            'status' : self.status.getjson(),
            'superior' : self.superior_info()
        }


class Detail(models.Model):
    serialnumber = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, db_column='employee', blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, db_column='program', blank=True, null=True)
    nominationdate = models.DateField(blank=True, null=True)
    whetherattended = models.BooleanField(blank=True, null=True)
    dateattended = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.employee} - {self.program}'

    def getjson(self):
        return {
            'serialnumber': self.serialnumber,
            'employee' : self.employee.getjson(),
            'program' : self.program.getjson(),
            'nominationdate' : self.nominationdate,
            'whetherattended' : self.whetherattended,
            'dateattended' : self.dateattended
        }
