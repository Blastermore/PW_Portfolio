from django.core.files.base import ContentFile
from artigos.models import Artigo

for obj in Artigo.objects.all():

    if obj.fotografia and obj.fotografia.name:

        try:
            # open file from storage backend
            obj.fotografia.open("rb")

            content = obj.fotografia.read()

            # save again to new storage
            obj.fotografia.save(
                obj.fotografia.name,
                ContentFile(content),
                save=True
            )

            obj.fotografia.close()

            print(f"Migrado: {obj}")

        except Exception as e:
            print(f"Erro em {obj}: {e}")