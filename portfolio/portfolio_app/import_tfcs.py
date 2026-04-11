import os
import json
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#setup do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_projeto.settings')
django.setup()

#importar modelos necessarios
from portfolio_app.models import (
    TFC,
    Autor,
    Docente,
    Licenciatura,
    Tecnologia,
    Competencia,
)

#Load do JSON com os dados dos TFCs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# vai buscar a pasta data
FILE_PATH = os.path.join(BASE_DIR, "data", "dados_tfcs.json")

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    tfcs_data = json.load(file)

def clean_list(lst):
    if not lst:
        return []
    return [x.strip() for x in lst if x and x.strip()]

#Iterar sobre os dados dos TFCs e criar os objetos no banco de dados
for item in tfcs_data:
    print(f"A importar TFC: {item['Titulo']}") #Debugging

    #Criar e associar a licenciatura
    lic_nome = item.get("Licenciaturas", ["Desconhecida"])[0]

    lic, _ = Licenciatura.objects.get_or_create(
        nome=lic_nome,
        defaults={
            "descricao": "",
            "creditos": 0,
            "instituicao": ""
        }
    )

    #Criar o TFC
    tfc = TFC.objects.create(
        titulo=item["Titulo"],
        resumo=item.get("Sumario", ""),
        link_pdf=item.get("Link_PDF", ""),
        imagem=item.get("Imagem", ""),
        rating=item.get("Rating", 0),
        licenciatura=lic
    )

    #Criar e associar os autores
    for nome in item.get("Autores", []):
        autor, _ = Autor.objects.get_or_create(nome=nome.strip())
        tfc.autores.add(autor)

    #Criar e associar os orientadores
    for nome in item.get("Orientadores", []):
        docente, _ = Docente.objects.get_or_create(nome=nome.strip())
        tfc.orientadores.add(docente)

    #Criar e associar as tecnologias
    for nome in item.get("Tecnologias", []):
        tech, _ = Tecnologia.objects.get_or_create(nome=nome.strip())
        tfc.tecnologias.add(tech)
    
    #Criar e associar as competências
    for nome in item.get("Competencias", []):
        comp, _ = Competencia.objects.get_or_create(nome=nome.strip())
        tfc.competencias.add(comp)

    tfc.licenciatura = lic
    tfc.save()

print("Importação concluída!") #Debugging