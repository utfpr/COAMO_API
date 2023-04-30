from rest_framework import serializers
from .models import Contato, Grupo, Telefone


class GrupoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grupo
        fields = '__all__'


class TelefoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telefone
        fields = [
            'id',
            'tipo_telefone',
            'número',
        ]


class ContatoSerializer(serializers.ModelSerializer):

    telefone_list = TelefoneSerializer(many=True)
    grupo = GrupoSerializer()

    class Meta:
        model = Contato
        fields = [
            'id',
            'nome',
            'grupo',
            'telefone_list',
            'empresa',
            'cargo',
            'email',
            'aniversário',
            'logradouro',
            'cidade',
            'estado',
            'cep',
            'observações',
        ]