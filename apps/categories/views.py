from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # A ordenação já está no Meta do modelo
    serializer_class = CategorySerializer
