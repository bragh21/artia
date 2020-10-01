from django.db import models
from app_home.models import Base


class Projeto(Base):

    def __str__(self):
        return self.nome
