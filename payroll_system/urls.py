from django.urls import path
from . import views

app_name = 'payroll_system'

urlpatterns = [
    path('templates/index/', views.index, name='index'),
    path('templates/signup/', views.signup, name='signup'),
    path('templates/login/', views.login, name='login'),
    path('templates/welcome/', views.welcome, name='welcome'),
    path('templates/compute/', views.compute, name='compute'),
    path('templates/display_payroll/',
         views.display_payroll, name='display_payroll'),
]
