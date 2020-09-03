from django.contrib import admin
from django.urls import path
from . import views

app_name = 'department_app'

urlpatterns = [
    path(
        'new-department/', 
        views.NewDepartmentView.as_view(), 
        name = 'new_department'
    ),

    path(
        'list-department/',
        views.DepartmentListView.as_view(),
        name = 'list_department'
    ),
]