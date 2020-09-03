from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.TestView.as_view()),
    path('list/', views.TestListView.as_view()),
    path('list_test/', views.ListTest.as_view()),
    path('add/', views.TestCreateView.as_view(), name = 'test_add'),
    path('resume/', views.ResumeFoundationView.as_view(), name = 'resume_foundation'),
]