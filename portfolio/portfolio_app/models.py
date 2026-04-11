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
    
#Modelo para um Docente
class Docente(models.Model):
    nome = models.CharField(max_length=200)
    mail = models.EmailField()
    websitePessoal = models.URLField()
    foto = models.ImageField(upload_to='fotos_docentes/')

    def __str__(self):
        return self.nome
    
#Modelo para um tecnologia
class Tecnologia(models.Model):
    nome = models.CharField(max_length=200)
    expertise = models.IntegerField()
    logo = models.ImageField(upload_to='logos_tecnologias/')
    websiteOficial = models.URLField()
    review = models.TextField()

    def __str__(self):
        return self.nome