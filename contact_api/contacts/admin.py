from django.contrib import admin
from .models import Contato, Grupo, Telefone, TipoTelefone
from django import forms


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 2


class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    inlines = [TelefoneInline]


admin.site.register(Contato, ContatoAdmin)
admin.site.register((Grupo, TipoTelefone))