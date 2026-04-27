from django.shortcuts import render, redirect
from .models import Licenciatura, UnidadeCurricular, Docente, Tecnologia, Competencia, Projeto, Gamejam, Formacao, MakingOf, MakingOfImagem, Autor, TFC
from .forms import ProjetoForm,TecnologiaForm, CompetenciaForm

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

def novo_tecnologia_view(request):
    form = TecnologiaForm(request.POST, request.FILES)
    if form.isValid():
        form.save()
        return redirect('tecnologias')

    context = {'form': form}
    return render(request, 'portfolio/novo_tecnologia.html', context)

def editar_tecnologia_view(request):
    tecnologia = Tecnologia.get(tecnologia, id=id)
    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)  # cria formulário com dados da instância autor

    context = {'form': form}
    return render(request, 'portfolio/editar_tecnologia.html', context)

def apagar_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.get(tecnologia, id=tecnologia_id)
    tecnologia.delete()
    
    return redirect('tecnologias')

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def novo_competencia_view(request):
    form = CompetenciaForm(request.POST, request.FILES)
    if form.isValid():
        form.save()
        return redirect('competencias')

    context = {'form': form}
    return render(request, 'portfolio/novo_competencia.html', context)

def editar_competencia_view(request):
    competencia = competencia.get(competencia, id=id)
    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)  # cria formulário com dados da instância autor

    context = {'form': form}
    return render(request, 'portfolio/editar_competencia.html', context)

def apagar_competencia_view(request, competencia_id):
    competencia = Competencia.get(competencia, id=competencia_id)
    competencia.delete()
    
    return redirect('competencias')

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def novo_projeto_view(request):
    form = ProjetoForm(request.POST, request.FILES)
    if form.isValid():
        form.save()
        return redirect('autores')

    context = {'form': form}
    return render(request, 'portfolio/projetoform.html', context)

def editar_projeto_view(request):
    projeto = Projeto.get(Projeto, id=id)
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)  # cria formulário com dados da instância autor

    context = {'form': form}
    return render(request, 'portfolio/projetoform.html', context)

def apagar_projeto_view(request):
    projeto = Projeto.get(Projeto, id=id)
    projeto.delete()
    
    return redirect('projetos')

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