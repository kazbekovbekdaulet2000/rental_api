import math
import random
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework.permissions import *
from rest_framework.views import APIView
from django.conf import settings
from django.core.cache import cache

from user.serializers.user_serializer import UserInfoSerializer, UserSerializer, UserUpdateSerializer


User = get_user_model()

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class UserView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_serializer_class(self):
        if not self.request.method == "GET":
            return UserUpdateSerializer
        return UserInfoSerializer

    def get_object(self):
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_OTP(mail):
    otp = generateOTP()
    cache.set(mail, otp, timeout=CACHE_TTL)


class ResetPassword(APIView):
    type = ''

    def post(self, request, *args, **kwargs):
        u = get_object_or_404(User, email=request.data['email'])
        if self.type == "force":
            send_OTP(request.data['email'])
            return Response({"time": cache.ttl(request.data['email'])}, status=status.HTTP_201_CREATED)
        if self.type == "reset":
            if not cache.get(request.data['email']):
                send_OTP(request.data['email'])
                return Response({"time": cache.ttl(request.data['email'])}, status=status.HTTP_201_CREATED)
            else:
                return Response({"time": cache.ttl(request.data['email'])}, status=status.HTTP_200_OK)
        if self.type == "confirm":
            if cache.get(request.data['email']) == None:
                return Response({"message": "Timeout"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            if cache.get(request.data['email']) == request.data['code']:
                if (request.data['password'] == request.data['re_password']):
                    user = get_object_or_404(User, email=request.data['email'])
                    user.set_password(request.data['password'])
                    user.save()
                    cache.delete(request.data['email'])
                    return Response({"message": "Пароль изменен"}, status=status.HTTP_201_CREATED)
            return Response({"message": "Код неправильный"}, status=status.HTTP_400_BAD_REQUEST)
