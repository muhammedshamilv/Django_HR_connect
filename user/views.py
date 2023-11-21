from dj_rest_auth.views import LoginView
from rest_framework import status
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from django.http import JsonResponse
from dj_rest_auth.registration.views import RegisterView
from user.serializers.user_serializers import CustomRegisterSerializer, CustomLoginSerializer, UserSerializer
# Create your views here.


class HealthCheck(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"Health": "ok"})


class Account(RegisterView):
    serializer_class = CustomRegisterSerializer


class EmployeeAcccount(RegisterView):
    serializer_class = UserSerializer

# class AccountUpdate(RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     lookup_field = "uuid"
#     queryset = User.objects.all()

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(
#             instance, data=request.data, partial=False)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({'message': 'User updated successfully', 'user': serializer.data}, status=status.HTTP_200_OK)


class UserLogin(LoginView):
    serializer_class = CustomLoginSerializer
