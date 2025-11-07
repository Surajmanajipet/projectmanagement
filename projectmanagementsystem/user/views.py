from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.


# We can do crud using generics class or easiest way is viewset

# class UserListCreate(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    

def home(req):
    return render(req,"landing.html")

def login(req):
    return render(req,"login.html")

def register(req):
    return render(req,"register.html")

def forgot(req):
    return render(req,"forgot-password.html")
