from rest_framework import serializers

from api.models import Categoria, Jogo


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"



class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = "__all__"
