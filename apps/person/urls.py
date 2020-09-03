from django.contrib import admin
from django.urls import path
from . import views

app_name = 'person_app'

urlpatterns = [
    path(
        '', 
        views.HomeView.as_view(), 
        name = 'home'
    ),
    path(
        'list-all-employee/', 
        views.ListAllEmployee.as_view(),
        name = 'employees',
    ),
    path(
        'list-by-area/<shortname>', 
        views.ListByAreaEmployee.as_view(),
        name = 'area_employee'
    ),
    path(
        'list-employee-admin', 
        views.ListEmployeeAdmin.as_view(),
        name = 'employee_admin'
    ),
    path(
        'list-by-job/<j>', 
        views.ListByJobEmployee.as_view(),
        name = 'list_by_job'
    ),
    path(
        'search-employee/', 
        views.ListEmployeeByKeyWord.as_view(),
        name = 'search_employee'
    ),   
    path(
        'skills/', 
        views.ListBySkill.as_view(),
        name = 'skills'
    ),
    path(
        'see-employee/<pk>', 
        views.EmployeeDetailView.as_view(),
        name = 'employee_detail'    
    ),
    path(
        'add-employee/', 
        views.EmployeeCreateView.as_view(),
        name = 'add_employee'
    ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name = 'correct'
    ),
    path(
        'update-employee/<pk>', 
        views.EmployeeUpdateView.as_view(), 
        name = 'modify_employee'
    ),
    path(
        'delete-employee/<pk>', 
        views.EmployeeDeleteView.as_view(), 
        name = 'delete_employee'
    ),
]