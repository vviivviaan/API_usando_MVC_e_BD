from rest_framework import serializers
from .models import Pessoa, Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'logradouro', 'numero', 'estado', 'cidade', 'bairro', 'pessoa']


class PessoaSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True, read_only=True)

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'idade', 'email', 'enderecos']
