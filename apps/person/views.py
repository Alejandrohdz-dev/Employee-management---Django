from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,DeleteView
from .models import Employee
from apps.department.models import Department
from .forms import EmployeeForm

class ListAllEmployee(ListView):
    template_name = 'person/list_all.html'
    paginate_by = 4
    context_object_name = 'employee'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        filter_list = Employee.objects.filter(
            first_name__icontains = key_word
        )
        return filter_list


class ListEmployeeAdmin(ListView):
    template_name = 'person/list_employee.html'
    paginate_by = 10
    context_object_name = 'employee'
    model = Employee


class ListByAreaEmployee(ListView):
    """List of employee of a specefic area"""
    template_name = 'person/list_by_area.html'
    context_object_name = 'employees'

    def get_queryset(self):

        area = self.kwargs['shortname']
        filter_list = Employee.objects.filter(
            department__short_name = area
        )
        
        return filter_list


class ListByJobEmployee(ListView):
    """List of employee of a specefic area"""
    template_name = 'person/list_by_job.html'
    
    def get_queryset(self):

        choise = self.kwargs['j']
        filter_list = Employee.objects.filter(
            job = choise
        )
        
        return filter_list


class ListEmployeeByKeyWord(ListView):
    """List of employees by keyword"""
    template_name = 'person/by_kword.html'
    context_object_name = 'employees'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        filter_list = Employee.objects.filter(
            first_name = key_word
        )
        print(filter_list)
        return filter_list


class ListBySkill(ListView):
    template_name = 'person/skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '1')
        employee = Employee.objects.get(
            id = key_word
        )
        return employee.skills.all()
        

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'person/detail_employee.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Employee of the month'
        return context


class SuccessView(TemplateView):
    template_name = "person/success.html"


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "person/add.html"
    form_class = EmployeeForm
    success_url = reverse_lazy('person_app:correct')

    def form_valid(self, form):
        employee = form.save()
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()
        return super(EmployeeCreateView, self).form_valid(form)


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "person/update.html"
    form_class = EmployeeForm
    success_url = reverse_lazy('person_app:correct')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmployeeUpdateView, self).form_valid(form)


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "person/delete.html"
    success_url = reverse_lazy('person_app:correct')


class HomeView(TemplateView):
    """ Initial view of the project """
    template_name = "home.html"
