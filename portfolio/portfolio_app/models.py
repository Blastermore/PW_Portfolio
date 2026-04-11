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

#Modelo para uma Unidade Curricular
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    creditos = models.IntegerField()
    avaliacao = models.IntegerField()
    ano = models.IntegerField()
    semestre = models.IntegerField()
    capa = models.ImageField(upload_to='capa_unidades/')

    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField('Docente')

    def __str__(self):
        return self.nome