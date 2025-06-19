from django.shortcuts import render
from rest_framework import viewsets # <-- Importar viewsets
from .models import Product # <-- Importar o modelo Product
from .serializers import ProductSerializer # <-- Importar o serializer ProductSerializer
   
class ProductViewSet(viewsets.ModelViewSet): # <-- Definir a classe ViewSet
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
