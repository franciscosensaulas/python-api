from django.shortcuts import render

from rest_framework import viewsets

from api.models import Categoria
from api.serializers import CategoriaSerializer

# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer