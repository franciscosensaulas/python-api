from django.shortcuts import render

from rest_framework import viewsets, generics

from api.models import Categoria, Cliente, Jogo
from api.serializers import CategoriaSerializer, ClienteSerializer, CustomTokenObtainPairSerializer, JogoPorCategoriaSerializer, JogoSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView

# ModelViewSet (GET, POST, PUT, PATCH, DELETE)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class JogoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

# POST
class ClienteCriarView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
class JogoPorCategoriaView(APIView):
    def get(self, request):
        jogos_por_categoria = Jogo.objects.values('categoria__nome').annotate(quantidade=Count('id'))
        serializer = JogoPorCategoriaSerializer(jogos_por_categoria, many=True)
        return Response(serializer.data)
