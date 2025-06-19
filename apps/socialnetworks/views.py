from django.shortcuts import render

# Create your views here.
from .models import Socialnetwork
from rest_framework import viewsets
from .serializers import SocialnetworkSerializer # Corrigido para .serializers

class SocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = Socialnetwork.objects.all()
    serializer_class = SocialnetworkSerializer
