from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
# These are the endpoints

class BeastView(generics.ListCreateAPIView):
    queryset = Beast.objects.all()
    serializer_class = BeastSerializer

class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class NpcView(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = NpcSerializer

class CharacterView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class SkillsView(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer