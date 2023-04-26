from django.db import models


class Grupo(models.Model):
    nome = models.CharField("nome do grupo", max_length=50)
    link_whats = models.CharField("grupo do WhatsApp", max_length=255,
                                  blank=True, null=True)

    def __str__(self):
        return self.nome


class TipoTelefone(models.Model):
    descrição = models.CharField(max_length=50)

    def __str__(self):
        return self.descrição


class Contato(models.Model):
    nome = models.CharField("nome completo", max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    telefones = models.ManyToManyField(TipoTelefone, through='Telefone')
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


class Telefone(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    tipo_telefone = models.ForeignKey(TipoTelefone,
                                      verbose_name="tipo de telefone",
                                      on_delete=models.CASCADE)
    número = models.CharField(max_length=25) # +55 44 9 9999 - 8888

    def __str__(self):
        return f'{self.tipo_telefone}: {self.número}'