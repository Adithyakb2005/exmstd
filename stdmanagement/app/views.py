from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .seializers import *
# Create your views here.

class std_view(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Std
