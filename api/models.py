from django.db import models

# Create your models here.
class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    desenvolvedora = models.CharField(max_length=50)
    data_lancamento = models.DateField()
    classificacao_metacritic = models.SmallIntegerField()
    tags = models.CharField(max_length=300)
    plataforma = models.CharField(max_length=300)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to="jogos", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="jogos")
    disponivel_venda = models.BooleanField()

    def __str__(self) -> str:
        return self.nome


from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)


class Cliente(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=10)