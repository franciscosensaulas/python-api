from rest_framework import serializers

from api.models import Categoria, Cliente, Jogo
from django.contrib.auth import get_user_model
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"



class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = "__all__"



User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Hash da senha
        user.save()
        return user

class ClienteSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Cliente
        fields = ['user', 'nome', 'cpf', 'data_nascimento', 'cep']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        cliente = Cliente.objects.create(user=user, **validated_data)
        return cliente


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.user.username

        return data