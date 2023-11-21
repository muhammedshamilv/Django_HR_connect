from django.shortcuts import render
from rest_framework.views import APIView
from staff.serializers.staff_serializers import ProjectSerializer, DesignationSerializer, ServiceRecordSerializer, PromotionHistorySerializer, AchievementHistorySerializer, TaskLogSerializer, GrievanceSerializer, UserProjectSerializer
from staff.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class ProjectAPI(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            serialized_project = ProjectSerializer(project).data
            return Response({"message": "project created successfully", "project": serialized_project}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = Project.objects.get(uuid=request.data.get('uuid'))
        except Project.DoesNotExist:
            return Response({"message": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Project updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = Project.objects.get(uuid=request.data.get('uuid'))
        except Project.DoesNotExist:
            return Response({"message": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class TaskLogAPI(APIView):
    serializer_class = TaskLogSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        task_logs = TaskLog.objects.all()
        serializer = TaskLogSerializer(task_logs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            task_log = serializer.save()
            serialized_task_log = TaskLogSerializer(task_log).data
            return Response({"message": "Task log created successfully", "task_log": serialized_task_log}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = TaskLog.objects.get(uuid=request.data.get('uuid'))
        except TaskLog.DoesNotExist:
            return Response({"message": "Task log not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskLogSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task log updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = TaskLog.objects.get(uuid=request.data.get('uuid'))
        except TaskLog.DoesNotExist:
            return Response({"message": "Task log not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Task log deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class GrievanceAPI(APIView):
    serializer_class = GrievanceSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        grievances = Grievance.objects.all()
        serializer = GrievanceSerializer(grievances, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            grievance = serializer.save()
            serialized_grievance = GrievanceSerializer(grievance).data
            return Response({"message": "Grievance created successfully", "grievance": serialized_grievance}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = Grievance.objects.get(uuid=request.data.get('uuid'))
        except Grievance.DoesNotExist:
            return Response({"message": "Grievance not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = GrievanceSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Grievance updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = Grievance.objects.get(uuid=request.data.get('uuid'))
        except Grievance.DoesNotExist:
            return Response({"message": "Grievance not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Grievance deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class UserProjectAPI(APIView):
    serializer_class = UserProjectSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_projects = UserProject.objects.all()
        serializer = UserProjectSerializer(user_projects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_project = serializer.save()
            serialized_user_project = UserProjectSerializer(user_project).data
            return Response({"message": "UserProject created successfully", "user_project": serialized_user_project}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = UserProject.objects.get(uuid=request.data.get('uuid'))
        except UserProject.DoesNotExist:
            return Response({"message": "UserProject not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProjectSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "UserProject updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = UserProject.objects.get(uuid=request.data.get('uuid'))
        except UserProject.DoesNotExist:
            return Response({"message": "UserProject not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "UserProject deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class AchievementHistoryAPI(APIView):
    serializer_class = AchievementHistorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        achievement_histories = AchievementHistory.objects.all()
        serializer = AchievementHistorySerializer(
            achievement_histories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            achievement_history = serializer.save()
            serialized_achievement_history = AchievementHistorySerializer(
                achievement_history).data
            return Response({"message": "AchievementHistory created successfully", "achievement_history": serialized_achievement_history}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = AchievementHistory.objects.get(
                uuid=request.data.get('uuid'))
        except AchievementHistory.DoesNotExist:
            return Response({"message": "AchievementHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AchievementHistorySerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "AchievementHistory updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = AchievementHistory.objects.get(
                uuid=request.data.get('uuid'))
        except AchievementHistory.DoesNotExist:
            return Response({"message": "AchievementHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "AchievementHistory deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class PromotionHistoryAPI(APIView):
    serializer_class = PromotionHistorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        promotion_histories = PromotionHistory.objects.all()
        serializer = PromotionHistorySerializer(promotion_histories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            promotion_history = serializer.save()
            serialized_promotion_history = PromotionHistorySerializer(
                promotion_history).data
            return Response({"message": "PromotionHistory created successfully", "promotion_history": serialized_promotion_history}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = PromotionHistory.objects.get(
                uuid=request.data.get('uuid'))
        except PromotionHistory.DoesNotExist:
            return Response({"message": "PromotionHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PromotionHistorySerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "PromotionHistory updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = PromotionHistory.objects.get(
                uuid=request.data.get('uuid'))
        except PromotionHistory.DoesNotExist:
            return Response({"message": "PromotionHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "PromotionHistory deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class ServiceRecordAPI(APIView):
    serializer_class = ServiceRecordSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        service_records = ServiceRecord.objects.all()
        serializer = ServiceRecordSerializer(service_records, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            service_record = serializer.save()
            serialized_service_record = ServiceRecordSerializer(
                service_record).data
            return Response({"message": "ServiceRecord created successfully", "service_record": serialized_service_record}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = ServiceRecord.objects.get(uuid=request.data.get('uuid'))
        except ServiceRecord.DoesNotExist:
            return Response({"message": "ServiceRecord not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceRecordSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "ServiceRecord updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = ServiceRecord.objects.get(uuid=request.data.get('uuid'))
        except ServiceRecord.DoesNotExist:
            return Response({"message": "ServiceRecord not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "ServiceRecord deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class DesignationAPI(APIView):
    serializer_class = DesignationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        designations = Designation.objects.all()
        serializer = DesignationSerializer(designations, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            designation = serializer.save()
            serialized_designation = DesignationSerializer(designation).data
            return Response({"message": "Designation created successfully", "designation": serialized_designation}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = Designation.objects.get(uuid=request.data.get('uuid'))
        except Designation.DoesNotExist:
            return Response({"message": "Designation not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = DesignationSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Designation updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = Designation.objects.get(uuid=request.data.get('uuid'))
        except Designation.DoesNotExist:
            return Response({"message": "Designation not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Designation deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
