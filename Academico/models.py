from django.db import models

# Create your models here.


class Curso(models.Model):

    codigo = models.CharField(primary_key=True, max_length=6)
    nome = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nome, self.creditos)
