from django.conf import settings
from django.db import models


class Post(models.Model):
    """Publicación / noticia del feed (mini-Twitter administrado)."""

    class Category(models.TextChoices):
        NOTICIAS = "noticias", "Noticias"
        CIRCULAR = "circular", "Circular"
        EVENTO = "evento", "Bogotá Eats"
        MARKETING = "marketing", "Marketing"

    title = models.CharField("título", max_length=200)
    category = models.CharField(
        "categoría", max_length=20, choices=Category.choices, default=Category.NOTICIAS
    )
    excerpt = models.CharField("resumen", max_length=300, blank=True)
    body = models.TextField("contenido", blank=True)
    image = models.ImageField("imagen", upload_to="posts/", blank=True, null=True)
    pdf = models.FileField("PDF", upload_to="posts/pdf/", blank=True, null=True)
    glyph = models.CharField("glifo", max_length=2, default="L")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        verbose_name="autor",
    )
    reactions = models.PositiveIntegerField("reacciones", default=0)
    is_published = models.BooleanField("publicado", default=True)
    created_at = models.DateTimeField("creado", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "publicación"
        verbose_name_plural = "publicaciones"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def has_pdf(self):
        return bool(self.pdf)


class Proposal(models.Model):
    """Propuesta o comentario enviado por un socio (NT-04)."""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="proposals",
        verbose_name="autor",
    )
    text = models.TextField("propuesta")
    created_at = models.DateTimeField("enviado", auto_now_add=True)

    class Meta:
        verbose_name = "propuesta"
        verbose_name_plural = "propuestas"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Propuesta de {self.author} · {self.created_at:%d %b}"
