from django.core.files.base import ContentFile
from portfolio_app.models import MakingOfImagem

for obj in MakingOfImagem.objects.all():

    if obj.imagem and obj.imagem.name:

        try:
            # open file from storage backend
            obj.imagem.open("rb")

            content = obj.imagem.read()

            # save again to new storage
            obj.imagem.save(
                obj.imagem.name,
                ContentFile(content),
                save=True
            )

            obj.imagem.close()

            print(f"Migrado: {obj}")

        except Exception as e:
            print(f"Erro em {obj}: {e}")