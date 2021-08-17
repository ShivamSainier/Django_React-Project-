from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Room
from .serial import RoomSerializer

class RoomView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer 