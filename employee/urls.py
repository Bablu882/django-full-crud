from django.urls import path
from .views import *

#BASEURL=http://127.0.0.1:8000/employee

urlpatterns = [
    #path('list/',views.Employee),
    path('add/',view_employee,name='add'),
    path('show/',show_all,name='show'),
    path('home/',view_home,name='index'),
    path('edit/<int:id>/',update_employ,name='edit'),
    path('base/',view_base),
    path('delete/<int:id>/',delete_employ,name='delete'),
    path('login/',view_login,name='login'),
    path('register/',view_register,name='register'),
    path('logout/',view_logout,name='logout'),
    path('index/',view_index,name='index'),
    path('home2/',view_home2,name='home2'),
    path('demo/',view_demo,name='demo'),
    path('login2',login2,name='login2'),
    path('register2',register_attemp,name='register2'),
    path('send-mail',sendmail,name='send-mail'),
    path('success',success,name='success'),


]
