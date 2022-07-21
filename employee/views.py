#from typing_extensions import Required

import profile
import uuid
from django.conf import settings
from django.forms import *
from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from employee.forms import EmployeeForm
from .models import *
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from .decorator import authenticate_user
import uuid
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def view_employee(request):
    if request.method=='GET':
        form_unbound=EmployeeForm()
        d1={'employ':form_unbound}
        resp=render(request,'employee/emplo.html',context=d1)
        return resp
    elif request.method=='POST':
        form_bound=EmployeeForm(request.POST,files=request.FILES)
        if form_bound.is_valid():
            d1={'employ':form_bound}
            form_bound.save()
            return redirect('/employee/show')#HttpResponse('<h1>Employee Details Added Successfully</h1>')
        else:
            form_bound=EmployeeForm()
            d1={'employ':form_bound}

            resp=render(request,'employee/emplo.html',context=d1)
            return resp 
@login_required(login_url='login')

def update_employ(request,id):
    employee=Employee.objects.get(id=id)
    form_unbound=EmployeeForm(instance=employee)
    if request.method=='POST':
        form_unbound=EmployeeForm(request.POST,instance=employee)
        if form_unbound.is_valid():
            form_unbound.save()
            return redirect('/employee/show')
    d1={'employ':form_unbound}
    resp=render(request,'employee/emplo.html',context=d1)
    return resp

@login_required(login_url='login')
def delete_employ(request,id):
    employee=Employee.objects.get(id=id)
    
    employee.delete()
    return render(request,'employee/delete.html')    




@login_required(login_url='login')
def show_all(request):
    u=Employee.objects.all()
    d1={'data':u}
    resp=render(request,'employee/poli.html',context=d1)
    return resp

def view_home(request):
    resp=render(request,'employee/home.html')    
    return resp


def view_base(request):
    resp=render(request,'employee/base.html') 
    return resp   


# @login_required(login_url='login')
# def login_poli(request):
#     resp=render(request,'employee/poli.html')
#     return resp

@authenticate_user
def view_register(request):
    if request.method=='GET':
        frm_unbound=UserCreationForm()
        d1={'form':frm_unbound}
        resp=render(request,'employee/register.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=UserCreationForm(request.POST)
        if frm_bound.is_valid():
            u=frm_bound.save()
            u.is_staff=True
            gr=Group.objects.get(name='bablu')
            u.groups.add(gr)



            #return HttpResponse("<h1>User registered successfully</h1>")    
            return redirect('/employee/login')
    else:
        frm_bound=UserCreationForm(request.POST)
        d1={'form':frm_bound}
    
        resp=render(request,'employee/register.html',context=d1)
        return resp




@authenticate_user         
def view_login(request):
    if request.method=="GET":
      resp=render(request,'employee/login.html')    
      return resp
    elif request.method=="POST":
        u_name=request.POST.get('txtusername','NA')
        u_pass=request.POST.get('txtpassword','NA')
        p=authenticate(request,username=u_name,password=u_pass)
        if p is not None:
            login(request,p)
            #resp=render(request,'employee/login2.html')
            #return resp
            return redirect('/employee/index')
            #return HttpResponse("<h1>Login Successfully</h1>")
        else:
             resp=render(request,'employee/login.html')
             return resp  



def view_logout(request):
    logout(request=request)
    # resp=render(request,'account/home.html')
    resp= render(request,'employee/logout.html')
    return resp

def view_index(request):
    resp=render(request,'employee/index.html')
    return resp

def view_home2(request):
    resp=render(request,'employee/home2.html')    
    return resp

def sendmail(request):
    return render(request,'employee/sent_mail.html')

def success(request):
    return render(request,'employee/success.html')    

def login2(request):
    return render(request,'employee/signup2.html')

def register2(request):
    return render(request,'employee/register2.html')    

def view_demo(request):
    resp=render(request,'employee/demo.html')    
    return resp    

def register_attemp(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username=username).first():
                messages.success(request,'username is taken ')
                return redirect('/employee/register2')

            if User.objects.filter(email=email).first():
                messages.success(request,'email is taken ')
                return redirect('/employee/register2')    
            user_obj=User(username=username ,email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token=str(uuid.uuid4())
            profile_obj=Profile.objects.create(user=user_obj,auth_token=auth_token)
            profile_obj.save()
            send_mail(email,auth_token)
            return redirect('/send-mail')
        except Exception as e:
            print(e)    
    return render(request,'employee/register2.html')





def verify_token(request):
    try:
        profile_obj=Profile.objects.filter(auth_token=auth_token).first()                
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request,'your account is already verified')
                return redirect('/login')
            profile_obj.is_verified=True  
            profile_obj.save()
            messages.success(request,'your account is already verified')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)   



def send_mail(request):
    subject="your account is verified "        
    messages=f'hi past the link to erified account http://127.0.0.1:8000/verify/{token}'
    email_from= settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,messages,email_from,recipient_list)






            
