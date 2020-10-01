from django.db import models

class Base(models.Model):

    nome = models.CharField(max_length=255)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True
