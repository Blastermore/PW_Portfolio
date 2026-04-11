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
    Docente,
    Licenciatura,
    UnidadeCurricular
)

#Load do JSON com os dados dos UCs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# vai buscar a pasta data
FILE_PATH = os.path.join(BASE_DIR, "data", "dados_ucs.json")

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    tfcs_data = json.load(file)

def clean_list(lst):
    if not lst:
        return []
    return [x.strip() for x in lst if x and x.strip()]

#Iterar sobre os dados dos UCs e criar os objetos no banco de dados
for item in tfcs_data:
    print(f"A importar UC: {item['Titulo']}") #Debugging

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

    #Criar o UC
    uc = UnidadeCurricular.objects.create(
        nome=item["curricularUnitName"],
        descricao=item.get("methodology", ""),
        creditos=item.get("ects", 0),
        avaliacao=item.get("Avaliacao", 0),
        ano=item.get("curricularYear", 0),
        semestre=None,
        capa=None,
        licenciatura=lic
    )

    #Criar e associar os docentes    
    for nome in item.get("Docentes", []):
        docente, _ = Docente.objects.get_or_create(nome=nome.strip())
        uc.docentes.add(docente)
    

    uc.licenciatura = lic
    uc.save()

print("Importação concluída!") #Debugging