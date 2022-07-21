from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.TextField(null=True,blank=True)
    Mobile_no=models.CharField(max_length=10)
    Company=models.CharField(max_length=50)
    Role=models.CharField(max_length=30)
    Image=models.ImageField(null=True,blank=True)
    Created_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Last_updated_date=models.DateTimeField(auto_now=True,blank=True,null=True)
    
    def __str__(self):
          return self.Name


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_verified=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username



