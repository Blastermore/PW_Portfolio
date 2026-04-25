from django.db import models

# Create your models here.

#Modelo para a licenciatura
class Licenciatura(models.Model):
    nome = models.CharField(max_length=200, blank = True, null=True)
    descricao = models.TextField(blank = True, null=True)
    creditos = models.IntegerField(blank = True, null=True)
    instituicao = models.CharField(max_length=200, blank = True, null=True)

    class Meta:
        verbose_name = "Licenciatura"
        verbose_name_plural = "Licenciaturas"

    def __str__(self):
        return self.nome

#Modelo para uma Unidade Curricular
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200, blank = True, null=True)
    descricao = models.TextField(blank = True, null=True)
    creditos = models.IntegerField(blank = True, null=True)
    avaliacao = models.IntegerField(blank = True, null=True)
    ano = models.IntegerField(blank = True, null=True)
    semestre = models.IntegerField(blank = True, null=True)
    capa = models.ImageField(upload_to='capa_unidades/', blank=True, null=True)

    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField('Docente', blank = True)

    class Meta:
        verbose_name = "Unidade Curricular"
        verbose_name_plural = "Unidades Curriculares"

    def __str__(self):
        return self.nome
    
#Modelo para um Docente
class Docente(models.Model):
    nome = models.CharField(max_length=200)
    mail = models.EmailField(blank = True, null=True)
    resumo = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_docentes/',blank=True, null=True)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return self.nome
    


#Modelo para um tecnologia
class Tecnologia(models.Model):
    nome = models.CharField(max_length=200)
    expertise = models.IntegerField()
    logo = models.ImageField(upload_to='logos_tecnologias/')
    websiteOficial = models.URLField()
    review = models.TextField()

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return self.nome

#Modelo para uma Competencia  
class Competencia(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank = True, null=True)
    expertise = models.IntegerField()

    tecnologias = models.ManyToManyField(Tecnologia, blank = True)

    class Meta:
        verbose_name = "Competência"
        verbose_name_plural = "Competências"

    def __str__(self):
        return self.nome
    

#Modelo para um Projeto
class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    ano = models.IntegerField(blank = True)
    semestre = models.IntegerField(blank = True)
    linkItch = models.URLField(blank = True)
    imagem = models.ImageField(upload_to='imagens_projetos/', blank = True)
    avaliacao = models.IntegerField(blank = True)

    UnidadeCurricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, blank = True, null = True)
    tecnologias = models.ManyToManyField(Tecnologia, blank = True)
    competencias = models.ManyToManyField(Competencia, blank = True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.nome

#Modelo para uma Gamejam
class Gamejam(models.Model):
    nome = models.CharField(max_length=200)
    nomeJogo = models.CharField(max_length=200, blank = True, null = True)
    descricao = models.TextField(blank = True, null = True)
    linkItch = models.URLField(blank = True)
    imagem = models.ImageField(upload_to='imagens_gamejams/', blank = True, null=True)
    classificacao = models.IntegerField(blank = True, null = True)

    tecnologias = models.ManyToManyField(Tecnologia, blank = True)
    competencias = models.ManyToManyField(Competencia, blank = True)

    class Meta:
        verbose_name = "Game Jam"
        verbose_name_plural = "Game Jams"

    def __str__(self):
        return self.nome
    
#Modelo para uma Formação
class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank = True, null=True)
    instituicao = models.CharField(max_length=200, blank = True, null=True)
    dataInicio = models.DateField(blank = True, null=True)
    dataFim = models.DateField(blank = True, null=True)
    nivel = models.IntegerField(blank = True, null=True)

    tecnologia = models.ManyToManyField(Tecnologia, blank = True)
    competencias = models.ManyToManyField(Competencia, blank = True)

    class Meta:
        verbose_name = "Formação"
        verbose_name_plural = "Formações"

    def __str__(self):
        return self.nome
    
#Modelo para o MakingOf
class MakingOf(models.Model):
    descricaoDecisao = models.TextField()
    errosEncontrados = models.TextField()
    justificacaoModelacao = models.TextField()
    usoAI = models.TextField()

    class Meta:
        verbose_name = "MakingOf"
        verbose_name_plural = "MakingOfs"

    def __str__(self):
        return f"MakingOf"
    
class MakingOfImagem(models.Model):
    imagem = models.ImageField(upload_to='imagens_makingof/')
    legenda = models.TextField()

    makingof = models.ForeignKey(MakingOf, on_delete=models.CASCADE, related_name='imagens')

    class Meta:
        verbose_name = "MakingOfImagem"
        verbose_name_plural = "MakingOfImagens"

    def __str__(self):
        return self.legenda

class Autor(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(blank = True, null=True)
    link_pdf = models.URLField(blank = True, null=True)
    imagem = models.ImageField(upload_to='imagens_tfcs/', blank = True, null=True)
    rating = models.IntegerField(blank = True, null=True)

    autores = models.ManyToManyField(Autor, blank = True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    orientadores = models.ManyToManyField(Docente, blank = True)
    tecnologias = models.ManyToManyField(Tecnologia, blank = True)
    competencias = models.ManyToManyField(Competencia, blank = True)

    class Meta:
        verbose_name = "TFC"
        verbose_name_plural = "TFCs"

    def __str__(self):
        return self.titulo

