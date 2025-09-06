from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username=None
    # Name=models.TextField(max_length=15,blank=True,null=True)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    ROLE_CHOICES=(
         ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    )
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    USERNAME_FIELD='email'  
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
        
    def __str__(self):
        return self.email
    


