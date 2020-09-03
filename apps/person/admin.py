from django.contrib import admin
from .models import Employee, Skills

admin.site.register(Skills)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'department',
        'job',
        'full_name'
    )
    def full_name(self,obj):
        return obj.first_name + ' ' + obj.last_name
    
    search_fields = ('first_name',)
    list_filter = ('department','job','skills')
    filter_horizontal = ('skills',)

admin.site.register(Employee, EmployeeAdmin)