## escola/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),   #  rota que abre diretamente a página home
    path('licenciaturas/', views.licenciaturas_view, name="licenciaturas"),
    path('unidadescurriculares/', views.unidadescurriculares_view, name="unidadescurriculares"),
    path('docentes/', views.docentes_view, name="docentes"),
    path('tecnologias/', views.tecnologias_view, name="tecnologias"),
    path('competencias/', views.competencias_view, name="competencias"),
    path('projetos/', views.projetos_view, name="projetos"),
    path('gamejams/', views.gamejams_view, name="gamejams"),
    path('formacoes/', views.formacoes_view, name="formacoes"),
    path('makingofs/', views.makingofs_view, name="makingofs"),
    path('makingofimagens/', views.makingofimagens_view, name="makingofimagens"), #posso tirar se depois n quiser dar uma pagina inteira as imagens
    path('autores/', views.autores_view, name="autores"),
    path('tfcs/', views.tfcs_view, name="tfcs"),
    path('projeto/novo', views.novo_projeto_view, name="novo_projeto"),
    path('projeto/<int:projeto_id>/editar', views.editar_projeto_view, name="editar_projeto"),
    path('projeto/<int:projeto_id>/apaga', views.apagar_projeto_view,name="apagar_projeto"),
]