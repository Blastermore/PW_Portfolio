from django.db import models

# Create your models here.

#Modelo para a licenciatura
class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    creditos = models.IntegerField()
    instituicao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
