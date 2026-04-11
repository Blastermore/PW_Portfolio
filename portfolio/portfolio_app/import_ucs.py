import os
import json
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_projeto.settings')
django.setup()

from portfolio_app.models import Docente, Licenciatura, UnidadeCurricular

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "dados_ucs.json")

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)


for item in data:

    for uc_data in item.get("ucList", []):

        nome_uc = uc_data.get("curricularUnitName")

        print(f"A importar UC: {nome_uc}")

        # licenciatura
        lic_nome = uc_data.get("courseName", "Desconhecida")

        lic, _ = Licenciatura.objects.get_or_create(
            nome=lic_nome,
            defaults={
                "descricao": "",
                "creditos": 0,
                "instituicao": ""
            }
        )

        # UC (evitar duplicados)
        uc, created = UnidadeCurricular.objects.get_or_create(
            nome=nome_uc,
            licenciatura=lic,
            defaults={
                "descricao": uc_data.get("methodology", ""),
                "creditos": uc_data.get("ects", 0),
                "avaliacao": None,
                "ano": uc_data.get("curricularYear", None),
                "semestre": None,
                "capa": None
            }
        )

        # docentes
        for nome in uc_data.get("teachers", []):  # ou "Docentes" dependendo do JSON
            docente, _ = Docente.objects.get_or_create(nome=nome.strip())
            uc.docentes.add(docente)

        uc.save()

print("Importação concluída!")