from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HelloWorldSerializer
from .models import HelloWorld

# Create your views here.
class HelloWorldViewSet(viewsets.ModelViewSet):
  queryset = HelloWorld.objects.all().order_by('language')
  serializer_class = HelloWorldSerializer
  
