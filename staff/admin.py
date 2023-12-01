from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Designation)
admin.site.register(Project)
admin.site.register(TaskLog)
admin.site.register(ServiceRecord)
admin.site.register(PromotionHistory)
admin.site.register(AchievementHistory)
admin.site.register(UserProject)
