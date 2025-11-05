from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, related_name='enderecos', on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"
