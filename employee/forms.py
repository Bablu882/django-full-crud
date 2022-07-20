from django import forms
from django.db import models
from .models import Employee




class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'



    def _init_(self,args,*kwargs):
     super()._init_(*args,**kwargs)
     for field in self.fields.values():
        field.widget.attrs["class"]="form-control"        
        
        



