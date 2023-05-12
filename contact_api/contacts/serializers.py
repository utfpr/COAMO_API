from rest_framework import serializers
from .models import Contato, Grupo, Telefone, TipoTelefone
from drf_writable_nested.serializers import WritableNestedModelSerializer


class GrupoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grupo
        fields = '__all__'


class TipoTelefoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoTelefone
        fields = '__all__'


class TelefoneSerializer(WritableNestedModelSerializer):
    tipo_telefone = TipoTelefoneSerializer()

    class Meta:
        model = Telefone
        fields = [
            'id',
            'tipo_telefone',
            'número',
        ]


class ContatoSerializer(WritableNestedModelSerializer):

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