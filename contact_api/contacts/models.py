from django.db import models


class Grupo(models.Model):
    nome = models.CharField("nome do grupo", max_length=50)
    link_whats = models.CharField("grupo do WhatsApp", max_length=255,
                                  blank=True, null=True)

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    tipo = models.CharField(max_length=50)
    número = models.CharField(max_length=15)

    def __str__(self):
        return self.número


class Contato(models.Model):
    nome = models.CharField("nome completo", max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    telefone = models.ManyToManyField(Telefone)
    empresa = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField("e-mail", max_length=100)
    aniversário = models.DateField(blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField("CEP", max_length=10, blank=True, null=True)
    observações = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome