from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Formulario de publicación pensado para un admin no técnico."""

    class Meta:
        model = Post
        fields = ["title", "category", "excerpt", "body", "image", "pdf"]
        labels = {
            "title": "Título",
            "category": "Categoría",
            "excerpt": "Texto / resumen",
            "body": "Contenido ampliado (opcional)",
            "image": "Imagen (opcional)",
            "pdf": "PDF (opcional)",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "field-input", "placeholder": "Ej: Resultados del trimestre"}
            ),
            "category": forms.Select(attrs={"class": "field-input"}),
            "excerpt": forms.Textarea(
                attrs={"class": "ta", "placeholder": "Escribe aquí la noticia..."}
            ),
            "body": forms.Textarea(
                attrs={"class": "ta", "placeholder": "Detalle adicional (opcional)"}
            ),
        }


class ImportForm(forms.Form):
    """Carga masiva de noticias desde un archivo Excel (.xlsx) o CSV."""

    archivo = forms.FileField(
        label="Archivo Excel o CSV",
        widget=forms.ClearableFileInput(
            attrs={"class": "field-input", "accept": ".xlsx,.csv"}
        ),
    )
