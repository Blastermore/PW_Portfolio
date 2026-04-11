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
    docentes = models.ManyToManyField('Docente', blank = True)

    def __str__(self):
        return self.nome
    
#Modelo para um Docente
class Docente(models.Model):
    nome = models.CharField(max_length=200)
    mail = models.EmailField()
    resumo = models.TextField(blank=True, null=True)
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

#Modelo para uma COmpetencia  
class Competencia(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    expertise = models.IntegerField()

    tecnologias = models.ManyToManyField(Tecnologia, blank = True)

    def __str__(self):
        return self.nome
    

#Modelo para um Projeto
class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    ano = models.IntegerField()
    semestre = models.IntegerField()
    linkItch = models.URLField()
    imagem = models.ImageField(upload_to='imagens_projetos/')
    avaliacao = models.IntegerField()

    UnidadeCurricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia, blank = True)
    competencias = models.ManyToManyField(Competencia, blank = True)

    def __str__(self):
        return self.nome

#Modelo para uma Gamejam
class Gamejam(models.Model):
    nome = models.CharField(max_length=200)
    nomeJogo = models.CharField(max_length=200)
    descricao = models.TextField()
    linkItch = models.URLField()
    imagem = models.ImageField(upload_to='imagens_gamejams/')
    classificacao = models.IntegerField()

    tecnologias = models.ManyToManyField(Tecnologia, blank = True)
    competencias = models.ManyToManyField(Competencia, blank = True)

    def __str__(self):
        return self.nome
    
#Modelo para uma Formação
class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    instituicao = models.CharField(max_length=200)
    dataInicio = models.DateField()
    dataFim = models.DateField()

    competencias = models.ManyToManyField(Competencia, blank = True)

    def __str__(self):
        return self.nome
    
#Modelo para o MakingOf
class MakingOf(models.Model):
    descricaoDecisao = models.TextField()
    errosEncontrados = models.TextField()
    justificacaoModelacao = models.TextField()
    usoAI = models.TextField()

    def __str__(self):
        return f"MakingOf"
    
class MakingOfImagem(models.Model):
    imagem = models.ImageField(upload_to='imagens_makingof/')
    legenda = models.TextField()

    makingof = models.ForeignKey(MakingOf, on_delete=models.CASCADE, related_name='imagens')

    def __str__(self):
        return self.legenda

class Autor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    link_pdf = models.URLField()
    imagem = models.ImageField(upload_to='imagens_tfcs/')
    rating = models.IntegerField()

    autores = models.ManyToManyField(Autor)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    orientadores = models.ManyToManyField(Docente, blank = True)
    tecnologias = models.ManyToManyField(Tecnologia, blank = True)
    competencias = models.ManyToManyField(Competencia, blank = True)

    def __str__(self):
        return self.titulo

