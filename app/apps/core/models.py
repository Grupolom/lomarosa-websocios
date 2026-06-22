from django.db import models


class Restaurant(models.Model):
    """Punto aliado / restaurante asociado (IN-02)."""

    name = models.CharField("nombre", max_length=120)
    zone = models.CharField("zona", max_length=120, blank=True)
    emoji = models.CharField("emoji", max_length=4, default="🥩")
    rating = models.PositiveSmallIntegerField("calificación", default=5)
    order = models.PositiveSmallIntegerField("orden", default=0)
    active = models.BooleanField("activo", default=True)

    class Meta:
        verbose_name = "punto aliado"
        verbose_name_plural = "puntos aliados"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    @property
    def stars(self):
        return "★" * self.rating


class Announcement(models.Model):
    """Banner superior / recordatorio de marketing editable (CI-05)."""

    text = models.CharField("texto", max_length=200)
    link_label = models.CharField("texto del enlace", max_length=60, blank=True)
    link_url = models.CharField("destino del enlace", max_length=200, blank=True)
    active = models.BooleanField("activo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "anuncio"
        verbose_name_plural = "anuncios"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text
