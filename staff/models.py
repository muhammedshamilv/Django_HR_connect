from django.db import models
from main.models import AbstractBaseModel


class Designation(AbstractBaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Project(AbstractBaseModel):
    name = models.CharField(max_length=255)


class TaskLog(AbstractBaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    current_date = models.DateField()
    updated_date = models.DateField()


class ServiceRecord(AbstractBaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2)


class PromotionHistory(AbstractBaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    date = models.DateField()
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)


class AchievementHistory(AbstractBaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    date = models.DateTimeField(auto_now=True)


class Grievance(AbstractBaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_requirement = models.BooleanField()


class UserProject(AbstractBaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
