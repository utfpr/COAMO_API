from django.http import HttpResponse
from markdown import markdown as md
from rest_framework import viewsets
from .models import Contato, Grupo
from .serializers import ContatoSerializer, GrupoSerializer


# def index(request):
#     curso = "Sistemas Integrados"
#     text = md(f'''
# # Curso de {curso}

# - Aula 03: trabalhando com dados na API do `Django`.
#     - Criando o model
#     - Adicionando dados pela API do model
#     - Adicionando dados pelo `Django admin`''')
#     return HttpResponse(text)


class ContatoViewSet(viewsets.ModelViewSet):
    serializer_class = ContatoSerializer
    queryset = Contato.objects.all()


class GrupoViewSet(viewsets.ModelViewSet):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.all()