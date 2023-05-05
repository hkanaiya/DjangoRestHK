from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelList(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer