from django.core.files.base import ContentFile
from portfolio_app.models import UnidadeCurricular

for obj in UnidadeCurricular.objects.all():

    if obj.capa and obj.capa.name:

        try:
            # open file from storage backend
            obj.capa.open("rb")

            content = obj.capa.read()

            # save again to new storage
            obj.capa.save(
                obj.capa.name,
                ContentFile(content),
                save=True
            )

            obj.capa.close()

            print(f"Migrado: {obj}")

        except Exception as e:
            print(f"Erro em {obj}: {e}")