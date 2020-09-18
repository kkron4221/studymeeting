from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('today_menu/', views.today_menu, name='today_menu'),
    path('plans/', views.plans, name='plans'),
    path('log/', views.log, name='log'),
]