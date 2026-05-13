from django.core.files.base import ContentFile
from portfolio_app.models import Docente

for obj in Docente.objects.all():

    if obj.foto and obj.foto.name:

        try:
            # open file from storage backend
            obj.foto.open("rb")

            content = obj.foto.read()

            # save again to new storage
            obj.foto.save(
                obj.foto.name,
                ContentFile(content),
                save=True
            )

            obj.foto.close()

            print(f"Migrado: {obj}")

        except Exception as e:
            print(f"Erro em {obj}: {e}")