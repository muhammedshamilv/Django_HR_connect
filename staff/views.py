from django.shortcuts import render
from rest_framework.views import APIView
from staff.serializers.staff_serializers import ProjectSerializer, DesignationSerializer, ServiceRecordSerializer, PromotionHistorySerializer, AchievementHistorySerializer, TaskLogSerializer, GrievanceSerializer, UserProjectSerializer
from staff.models import *
from user.models import *

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.


class ProjectAPI(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

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
            instance = Project.objects.get(id=request.data.get('id'))
        except Project.DoesNotExist:
            return Response({"message": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = ProjectSerializer(
                instance).data
            return Response({"message": "Project updated successfully.", "data": serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = Project.objects.get(id=request.data.get('id'))
        except Project.DoesNotExist:
            return Response({"message": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class GetProject(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsAdminUser]


class TaskLogAPI(generics.ListCreateAPIView):
    queryset = TaskLog.objects.all()
    serializer_class = TaskLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.data.get("user_id")
        return TaskLog.objects.filter(user=user_id)

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        serializer = self.serializer_class(data=request.data)
        user = User.objects.filter(id=user_id).first()
        if serializer.is_valid():
            task_log = serializer.save(user=user)
            serialized_task_log = TaskLogSerializer(task_log).data
            return Response({"message": "Task log created successfully", "task_log": serialized_task_log}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskLogDetailAPI(APIView):
    queryset = TaskLog.objects.all()
    serializer_class = TaskLogSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            instance = TaskLog.objects.get(id=kwargs.get('id'))
        except TaskLog.DoesNotExist:
            return Response({"message": "Task log not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskLogSerializer(
            instance).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            instance = TaskLog.objects.get(id=kwargs.get('id'))
        except TaskLog.DoesNotExist:
            return Response({"message": "Task log not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskLogSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = TaskLogSerializer(
                instance).data
            return Response({"message": "Task log updated successfully.", "data": serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = TaskLog.objects.get(id=kwargs.get('id'))
        except TaskLog.DoesNotExist:
            return Response({"message": "Task log not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Task log deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class GetTaskLog(generics.RetrieveAPIView):
    queryset = TaskLog.objects.all()
    serializer_class = TaskLogSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class GetAllTaskLog(generics.ListAPIView):
    queryset = TaskLog.objects.all()
    serializer_class = TaskLogSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class GrievanceAPI(generics.ListCreateAPIView):
    queryset = Grievance.objects.all()
    serializer_class = GrievanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.get('user_id')
        return Grievance.objects.filter(user=user_id)

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        serializer = self.serializer_class(data=request.data)
        user = User.objects.filter(id=user_id).first()
        if serializer.is_valid():
            grievance = serializer.save(user=user)
            serialized_grievance = GrievanceSerializer(grievance).data
            return Response({"message": "Grievance created successfully", "grievance": serialized_grievance}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GrievanceDetailAPI(APIView):
    queryset = Grievance.objects.all()
    serializer_class = GrievanceSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            instance = Grievance.objects.get(id=kwargs.get('id'))
        except Grievance.DoesNotExist:
            return Response({"message": "Task log not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = GrievanceSerializer(
            instance).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            instance = Grievance.objects.get(id=kwargs.get('id'))
        except Grievance.DoesNotExist:
            return Response({"message": "Grievance not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = GrievanceSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = GrievanceSerializer(
                instance).data
            return Response({"message": "Grievance updated successfully.", "data": serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = Grievance.objects.get(id=kwargs.get('id'))
        except Grievance.DoesNotExist:
            return Response({"message": "Grievance not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Grievance deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class GetGrievance(generics.RetrieveAPIView):
    queryset = Grievance.objects.all()
    serializer_class = GrievanceSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class GetAllGrievance(generics.ListAPIView):
    queryset = Grievance.objects.all()
    serializer_class = GrievanceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserProjectAPI(APIView):
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_projects = UserProject.objects.filter(
            user=request.data.get("user_id")).all()
        serializer = UserProjectSerializer(user_projects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        projects = request.data.get('projects', [])
        user = User.objects.filter(id=user_id).first()
        user_projects = []
        for project_id in projects:
            data = {'user': user_id, 'project': project_id}
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                user_project = serializer.save(user=user)
                user_projects.append(user_project)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serialized_user_projects = UserProjectSerializer(
            user_projects, many=True).data
        return Response({"message": "UserProjects created successfully", "user_projects": serialized_user_projects}, status=status.HTTP_201_CREATED)


class DeleteUserProjectAPI(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        try:
            instance = UserProject.objects.get(id=kwargs.get('id'))
        except UserProject.DoesNotExist:
            return Response({"message": "UserProject not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "UserProject deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class GetAllUserProject(generics.ListAPIView):
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class AchievementHistoryAPI(APIView):
    serializer_class = AchievementHistorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        achievement_histories = AchievementHistory.objects.filter(
            user=user_id).all()
        serializer = AchievementHistorySerializer(
            achievement_histories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        user = User.objects.filter(id=user_id).first()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            achievement_history = serializer.save(user=user)
            serialized_achievement_history = AchievementHistorySerializer(
                achievement_history).data
            return Response({"message": "AchievementHistory created successfully", "achievement_history": serialized_achievement_history}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AchievementHistoryDetailAPI(APIView):
    queryset = AchievementHistory.objects.all()
    serializer_class = AchievementHistorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            instance = AchievementHistory.objects.get(
                id=kwargs.get('id'))
        except AchievementHistory.DoesNotExist:
            return Response({"message": "AchievementHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AchievementHistorySerializer(
            instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            instance = AchievementHistory.objects.get(
                id=kwargs.get('id'))
        except AchievementHistory.DoesNotExist:
            return Response({"message": "AchievementHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AchievementHistorySerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = AchievementHistorySerializer(
                instance).data
            return Response({"message": "AchievementHistory updated successfully.", "data": serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = AchievementHistory.objects.get(
                id=kwargs.get('id'))
        except AchievementHistory.DoesNotExist:
            return Response({"message": "AchievementHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "AchievementHistory deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class GetAllAchievement(generics.ListAPIView):
    queryset = AchievementHistory.objects.all()
    serializer_class = AchievementHistorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
# complete

# in progress


class PromotionHistoryAPI(APIView):
    serializer_class = PromotionHistorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        promotion_histories = PromotionHistory.objects.filter(
            user=request.data.get("user_id")).all()
        serializer = PromotionHistorySerializer(promotion_histories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        user = User.objects.filter(id=request.data.get("user_id")).first()
        if serializer.is_valid():
            promotion_history = serializer.save(user=user)
            serialized_promotion_history = PromotionHistorySerializer(
                promotion_history).data
            return Response({"message": "PromotionHistory created successfully", "promotion_history": serialized_promotion_history}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PromotionHistoryDetailAPI(APIView):
    serializer_class = PromotionHistorySerializer
    queryset = PromotionHistory.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            instance = PromotionHistory.objects.get(
                id=kwargs.get('id'))
        except PromotionHistory.DoesNotExist:
            return Response({"message": "PromotionHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PromotionHistorySerializer(
            instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            instance = PromotionHistory.objects.get(
                id=kwargs.get('id'))
        except PromotionHistory.DoesNotExist:
            return Response({"message": "PromotionHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PromotionHistorySerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = PromotionHistorySerializer(
                instance).data
            return Response({"message": "PromotionHistory updated successfully.", "data": serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = PromotionHistory.objects.get(
                id=request.data.get('id'))
        except PromotionHistory.DoesNotExist:
            return Response({"message": "PromotionHistory not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "PromotionHistory deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class PromotionAllHistory(generics.ListAPIView):
    queryset = PromotionHistory.objects.all()
    serializer_class = PromotionHistorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ServiceRecordAPI(APIView):
    serializer_class = ServiceRecordSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

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
            instance = ServiceRecord.objects.get(id=request.data.get('id'))
        except ServiceRecord.DoesNotExist:
            return Response({"message": "ServiceRecord not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceRecordSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = ServiceRecordSerializer(
                instance).data
            return Response({"message": "ServiceRecord updated successfully.", "data": serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = ServiceRecord.objects.get(id=request.data.get('id'))
        except ServiceRecord.DoesNotExist:
            return Response({"message": "ServiceRecord not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "ServiceRecord deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class ServiceRecordDetailAPI(generics.RetrieveAPIView):
    queryset = ServiceRecord.objects.all()
    serializer_class = ServiceRecordSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsAdminUser]


class DesignationAPI(APIView):
    serializer_class = DesignationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        designations = Designation.objects.all()
        serializer = DesignationSerializer(designations, many=True)
        return Response(serializer.data)


class DesignationPost(generics.CreateAPIView):
    serializer_class = DesignationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            designation = serializer.save()
            serialized_designation = DesignationSerializer(designation).data
            return Response({"message": "Designation created successfully", "designation": serialized_designation}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DesignationDetailAPI(APIView):
    serializer_class = DesignationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, *args, **kwargs):
        try:
            instance = Designation.objects.get(id=kwargs.get('id'))
        except Designation.DoesNotExist:
            return Response({"message": "Designation not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = DesignationSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = DesignationSerializer(
                instance).data
            return Response({"message": "Designation updated successfully.", "data": serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = Designation.objects.get(id=kwargs.get('id'))
        except Designation.DoesNotExist:
            return Response({"message": "Designation not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Designation deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
