from django.contrib import admin
from .models import Department, Cadre, EmployeeStatus, ProgramType, Program, Employee, Detail


# admin.site.register(Department)
admin.site.register(Cadre)
admin.site.register(EmployeeStatus)
admin.site.register(ProgramType)
# admin.site.register(Program)
# admin.site.register(Employee)
# admin.site.register(Detail)

class ProgramDetailInline(admin.TabularInline):
    model = Detail


# Define the admin class
class DepartmentAdmin(admin.ModelAdmin):
        list_display = ('code', 'name')

# Register the admin class with the associated model
admin.site.register(Department, DepartmentAdmin)

# Define the admin class
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
        list_display = ('code', 'description', 'minimumeligibility', 'maximumeligibility', 'type')
        inlines = [ProgramDetailInline]

# Register the Admin classes for Employee using the decorator
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('psnumber', 'initial', 'firstname', 'middlename', 'lastname', 'cadre', 'department', 'status', 'superior')
    list_filter = ('department', 'status')
    # fields = ['psnumber', 'initial', ('firstname', 'middlename', 'lastname'), ('cadre', 'department'), ('status', 'superior')]
    fieldsets = (
        (None, {
            'fields' : ('psnumber', 'initial')
        }),
        ('Name', {
            'fields': ('firstname', 'middlename', 'lastname')
        }),
        (None, {
            'fields':  ('cadre', 'department')
        }),
        (None, {
            'fields': ('status', 'superior')
        }),
    )
    inlines = [ProgramDetailInline]



# Register the Admin classes for Detail using the decorator
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    pass
