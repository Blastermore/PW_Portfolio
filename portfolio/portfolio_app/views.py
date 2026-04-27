from django.shortcuts import render
from .models import Licenciatura, UnidadeCurricular, Docente, Tecnologia, Competencia, Projeto, Gamejam, Formacao, MakingOf, MakingOfImagem, Autor, TFC
from .forms import ProjetoForm

# Create your views here.

def home_view(request):
    return render(request, 'portfolio/home.html')

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def unidadescurriculares_view(request):
    unidadescurriculares = UnidadeCurricular.objects.all()
    return render(request, 'portfolio/unidadescurriculares.html', {'unidadescurriculares': unidadescurriculares})

def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, 'portfolio/docentes.html', {'docentes': docentes})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def projeto_create(request):
    form = ProjetoForm(request.POST, request.Files)
    return render(request, 'portfolio/projetoform.html', {'form': form})

def gamejams_view(request):
    gamejams = Gamejam.objects.all()
    return render(request, 'portfolio/gamejams.html', {'gamejams': gamejams})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def makingofs_view(request):
    makingofs = MakingOf.objects.all()
    return render(request, 'portfolio/makingofs.html', {'makingofs': makingofs})

def makingofimagens_view(request):
    makingofimagens = MakingOfImagem.objects.all()
    return render(request, 'portfolio/makingofimagens.html', {'makingofimagens': makingofimagens})

def autores_view(request):
    autores = Autor.objects.all()
    return render(request, 'portfolio/autores.html', {'autores': autores})

def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})