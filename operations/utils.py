from PIL import Image
import io
from django.core.files.base import ContentFile

def compress_image(uploaded_image, max_size=(800, 800)):
    img = Image.open(uploaded_image)

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.thumbnail(max_size, Image.LANCZOS)

    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=70)
    return ContentFile(buffer.getvalue(), name=uploaded_image.name)
