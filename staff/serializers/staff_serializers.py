from rest_framework import serializers
from staff.models import *


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TaskLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskLog
        fields = "__all__"


class ServiceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRecord
        fields = "__all__"


class PromotionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionHistory
        fields = "__all__"


class AchievementHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementHistory
        fields = "__all__"


class GrievanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = "__all__"


class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = "__all__"
