from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artigo(models.Model):
    titulo = models.CharField(max_length = 100)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank = True, null =True)
    link_externo = models.URLField(blank = True, null = True)
    data_criacao = models.DateTimeField(auto_now = True)
    
    autor = models.ForeignKey(User, on_delete=CASCADE, related_names = 'artigos')
    likes = models.ForeignKey(User, blank =True, related_names = 'likes_artigos')

    def total_total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add = True)
    
    artigo = models.ForeignKey(Artigo, on_delete=CASCADE, related_names = 'comentarios')
    autor = models.ForeignKey(User, on_delete='CASCADE', related_name = 'comentarios')