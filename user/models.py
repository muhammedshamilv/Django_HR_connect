from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import AbstractBaseModel
from staff.models import Designation


class User(AbstractUser, AbstractBaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    code = models.BigIntegerField(default=0)
    date_of_birth = models.DateField(null=True)
    address = models.TextField()
    blood_group = models.CharField(max_length=255)
    resume = models.FileField(null=True)
    password = models.CharField(max_length=255)
    date_of_joining = models.DateField(auto_now=True)
    designation = models.ForeignKey(
        Designation, on_delete=models.CASCADE, null=True)
    current_designation = models.ForeignKey(
        Designation, related_name='current_users', on_delete=models.CASCADE, null=True)
