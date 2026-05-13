from django.core.files.base import ContentFile
from portfolio_app.models import Tecnologia

for obj in Tecnologia.objects.all():

    if obj.logo and obj.logo.name:

        try:
            # open file from storage backend
            obj.logo.open("rb")

            content = obj.logo.read()

            # save again to new storage
            obj.logo.save(
                obj.logo.name,
                ContentFile(content),
                save=True
            )

            obj.logo.close()

            print(f"Migrado: {obj}")

        except Exception as e:
            print(f"Erro em {obj}: {e}")