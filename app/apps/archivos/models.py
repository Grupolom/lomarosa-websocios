from django.conf import settings
from django.db import models


class Document(models.Model):
    """Documento personal de un socio (AR-01..05). Solo el admin lo gestiona."""

    class Status(models.TextChoices):
        VIGENTE = "vigente", "Vigente"
        OFICIAL = "oficial", "Oficial"
        ACTIVO = "activo", "Activo"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents",
        verbose_name="socio",
    )
    name = models.CharField("nombre", max_length=200)
    pdf = models.FileField("PDF", upload_to="documentos/", blank=True, null=True)
    size_label = models.CharField("tamaño", max_length=20, blank=True)
    status = models.CharField(
        "estado", max_length=10, choices=Status.choices, default=Status.VIGENTE
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploaded_documents",
        verbose_name="subido por",
    )
    created_at = models.DateTimeField("creado", auto_now_add=True)

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} · {self.owner}"
