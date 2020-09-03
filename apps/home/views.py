from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Test
from .forms import TestForm

class TestView(TemplateView):
    template_name = 'home/home.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'
    
class TestListView(ListView):
    template_name = 'home/list.html'
    queryset = ['1','20','30','40']
    context_object_name = 'NumList'

class ListTest(ListView):
    template_name = 'home/list_test.html'
    model = Test
    context_object_name = 'list_test'
    
class TestCreateView(CreateView):
    model = Test
    template_name = "home/add.html"
    # fields = ['title','subtitle','quantity']
    form_class = TestForm
    success_url = '/'