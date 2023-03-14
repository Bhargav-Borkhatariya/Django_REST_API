from django.contrib import admin
from Employee_CRUD.models import Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
