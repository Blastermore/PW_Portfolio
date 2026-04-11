import os
import json
import django

#setup do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
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
FILE_PATH = 'tfcs.json'

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    tfcs_data = json.load(file)

def clean_list(lst):
    if not lst:
        return []
    return [x.strip() for x in lst if x and x.strip()]

#Iterar sobre os dados dos TFCs e criar os objetos no banco de dados
for item in tfcs_data:
    print(f"A importar TFC: {item['titulo']}") #Debugging

    #Criar o TFC
    tfc = TFC.objects.create(
        titulo=item["Titulo"],
        resumo=item.get("Sumario", ""),
        link_pdf=item.get("Link_PDF", ""),
        imagem=item.get("Imagem", ""),
        rating=item.get("Rating", 0)
    )

    #Criar e associar os autores
    for nome in item.get("Autores", []):
        autor, _ = Autor.objects.get_or_create(nome=nome.strip())
        tfc.autores.add(autor)

    #Criar e associar os orientadores
    for nome in item.get("Orientadores", []):
        docente, _ = Docente.objects.get_or_create(nome=nome.strip())
        tfc.orientadores.add(docente)

    #Criar e associar a licenciatura
    for nome in item.get("Licenciaturas", []):
        lic, _ = Licenciatura.objects.get_or_create(nome=nome)
        tfc.licenciatura = lic
        tfc.save()

    #Criar e associar as tecnologias
    for nome in item.get("Tecnologias_Usadas", []):
        tech, _ = Tecnologia.objects.get_or_create(nome=nome)
        tfc.tecnologias.add(tech)
    
    #Criar e associar as competências
    for nome in item.get("Areas_Competencias", []):
        comp, _ = Competencia.objects.get_or_create(nome=nome)
        tfc.competencias.add(comp)

    tfc.save()

print("Importação concluída!") #Debugging