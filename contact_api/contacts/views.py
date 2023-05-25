from django.http import HttpResponse
from markdown import markdown as md
from rest_framework import viewsets
from .models import Contato, Grupo
from .serializers import ContatoSerializer, GrupoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from twilio.rest import Client
from .twilio_data import SID, TOKEN, FROM


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


class SendMsgView(APIView):

    def post(self, request, format=None):
        account_sid = SID
        auth_token = TOKEN
        client = Client(account_sid, auth_token)

        numero_destino = request.data.get('phone')
        mensagem = request.data.get('message')

        print(numero_destino, mensagem)

        message = client.messages.create(
            body=mensagem,
            from_=f'whatsapp:{FROM}',
            to=f'whatsapp:{numero_destino}'
        )

        return Response({'message_sid': message.sid})
