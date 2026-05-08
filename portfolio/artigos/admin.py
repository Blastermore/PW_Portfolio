from django.contrib import admin
from .models import Artigo, Comentario

# Register your models here.

admin.site.register(Artigo)
admin.site.register(Comentario)