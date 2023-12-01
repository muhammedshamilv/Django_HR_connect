from django.contrib import admin
from .models import *
# Register your models here.


class UserModel(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'code'
    )


admin.site.register(User, UserModel)
