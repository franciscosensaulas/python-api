from django.shortcuts import render

from rest_framework import viewsets, generics

from api.models import Categoria, Cliente, Jogo
from api.serializers import CategoriaSerializer, ClienteSerializer, CustomTokenObtainPairSerializer, JogoSerializer

# ModelViewSet (GET, POST, PUT, PATCH, DELETE)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

# POST
class ClienteCriarView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer