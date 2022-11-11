from django.shortcuts import render
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import permissions
from rest_framework import generics



# Create your views here.



class RegisterAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        })