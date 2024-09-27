from django.shortcuts import render
from rest_framework import viewsets

from.models import Car
from.serializers import CarSerializers

class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializers_class = CarSerializers