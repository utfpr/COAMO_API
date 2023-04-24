from django.contrib import admin
from .models import Contato, Grupo, Telefone


admin.site.register((Contato, Grupo, Telefone))