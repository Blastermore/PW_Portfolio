from django.core.files.base import ContentFile
from escola.models import Curso

for obj in Curso.objects.all():
    if not obj.imagem:
        continue

    try:
        obj.imagem.open()  # ensures file is accessible

        file_content = obj.imagem.read()
        filename = obj.imagem.name.split("/")[-1]

        obj.imagem.save(
            filename,
            ContentFile(file_content),
            save=True
        )

        print(f"Uploaded: {obj.id}")

    except Exception as e:
        print(f"Error with {obj.id}: {e}")