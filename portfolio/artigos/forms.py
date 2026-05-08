from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from django import forms
from .models import Artigo, Comentario


class ArtigoForm(forms.ModelForm):

    class Meta:
        model = Artigo

        fields = [
            'titulo',
            'texto',
            'fotografia',
            'link_externo'
        ]


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario

        fields = ['texto']