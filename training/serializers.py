from training.models import Department, Cadre, EmployeeStatus, ProgramType, Program, Employee, Detail
from rest_framework import serializers

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['psnumber',
                  'initial',
                  'firstname',
                  'middlename',
                  'lastname',
                  'cadre_code',
                  'department_code',
                  'status_code',
                  'superior_psnumber',
                  'fullname']
