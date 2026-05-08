from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Artigo
from .forms import ArtigoForm, ComentarioForm


def lista_artigos(request):

    artigos = Artigo.objects.all().order_by('-data_criacao')

    return render(request, 'artigos/lista_artigos.html', {
        'artigos': artigos
    })


def detalhe_artigo(request, artigo_id):

    artigo = get_object_or_404(Artigo, id=artigo_id)

    comentarios = artigo.comentarios.all()

    form = ComentarioForm()

    return render(request, 'artigos/detalhe_artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form
    })


@login_required
def criar_artigo(request):

    if not request.user.groups.filter(name='autores').exists():
        return redirect('lista_artigos')

    form = ArtigoForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        artigo = form.save(commit=False)

        artigo.autor = request.user

        artigo.save()

        return redirect('lista_artigos')

    return render(request, 'artigos/criar_artigo.html', {
        'form': form
    })


@login_required
def editar_artigo(request, artigo_id):

    artigo = get_object_or_404(Artigo, id=artigo_id)

    if artigo.autor != request.user:
        return redirect('lista_artigos')

    form = ArtigoForm(
        request.POST or None,
        request.FILES or None,
        instance=artigo
    )

    if form.is_valid():

        form.save()

        return redirect('detalhe_artigo', artigo.id)

    return render(request, 'artigos/editar_artigo.html', {
        'form': form
    })


@login_required
def adicionar_comentario(request, artigo_id):

    artigo = get_object_or_404(Artigo, id=artigo_id)

    form = ComentarioForm(request.POST)

    if form.is_valid():

        comentario = form.save(commit=False)

        comentario.artigo = artigo

        comentario.autor = request.user

        comentario.save()

    return redirect('detalhe_artigo', artigo.id)


@login_required
def like_artigo(request, artigo_id):

    artigo = get_object_or_404(Artigo, id=artigo_id)

    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)

    # volta para onde veio
    next_url = request.GET.get('next')

    if next_url:
        return redirect(next_url)

    else:
        return redirect('lista_artigos')

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        next_url = request.GET.get('next')

        if user is not None:

            login(request, user)

            if next_url:

                return redirect(next_url)

            
            else:
                return redirect('lista_artigos')

        else:

            return render(request, 'artigos/login.html', {
                'erro': 'Credenciais inválidas'
            })

    return render(request, 'artigos/login.html')


def logout_view(request):

    logout(request)

    return redirect('login')