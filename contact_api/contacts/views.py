from django.http import HttpResponse
from markdown import markdown as md


def index(request):
    curso = "Sistemas Integrados"
    text = md(f'''
# Curso de {curso}

- Aula 03: trabalhando com dados na API do `Django`.
    - Criando o model
    - Adicionando dados pela API do model
    - Adicionando dados pelo `Django admin`''')
    return HttpResponse(text)