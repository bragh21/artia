from django.db import models
from app_home.models import Base


class Atividade(Base):

    projeto = models.ForeignKey('app_projeto.Projeto', on_delete=models.CASCADE)
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome} - {self.projeto}'
    
