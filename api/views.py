from django.shortcuts import render

from rest_framework import viewsets

from api.models import Categoria, Jogo
from api.serializers import CategoriaSerializer, JogoSerializer

# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer