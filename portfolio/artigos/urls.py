from django.urls import path
from . import views

urlpatterns = [

    path('', views.lista_artigos, name='lista_artigos'),
    path('<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('criar/', views.criar_artigo, name='criar_artigo'),
    path('editar/<int:artigo_id>/', views.editar_artigo, name='editar_artigo'),
    path('comentario/<int:artigo_id>/', views.adicionar_comentario, name='adicionar_comentario'),
    path( 'like/<int:artigo_id>/', views.like_artigo, name='like_artigo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]