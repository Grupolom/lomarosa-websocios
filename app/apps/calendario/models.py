from django.db import models

MESES_ABBR = {
    1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic",
}


class Event(models.Model):
    """Evento o reunión del calendario Lomarosa."""

    class Platform(models.TextChoices):
        TEAMS = "teams", "Microsoft Teams"
        MEET = "meet", "Google Meet"
        ZOOM = "zoom", "Zoom"
        PRESENCIAL = "presencial", "Presencial"

    class Tag(models.TextChoices):
        OBLIGATORIA = "obligatoria", "Obligatoria"
        RECOMENDADA = "recomendada", "Recomendada"
        SOLO_SOCIOS = "solo_socios", "Solo socios"
        COMERCIAL = "comercial", "Comercial"

    # color de acento usado en la UI (borde de la tarjeta)
    COLOR_BY_TAG = {
        "obligatoria": "terra",
        "recomendada": "gold",
        "solo_socios": "green",
        "comercial": "moss",
    }

    title = models.CharField("título", max_length=200)
    description = models.TextField("descripción", blank=True)
    date = models.DateField("fecha")
    time = models.TimeField("hora", null=True, blank=True)
    end_time = models.TimeField("hora fin", null=True, blank=True)
    location = models.CharField("lugar", max_length=200, blank=True)
    platform = models.CharField(
        "plataforma", max_length=20, choices=Platform.choices, blank=True
    )
    meet_url = models.URLField("enlace de reunión", blank=True)
    tag = models.CharField(
        "tipo", max_length=20, choices=Tag.choices, default=Tag.RECOMENDADA
    )
    reminder = models.BooleanField("recordatorio activo", default=True)
    created_at = models.DateTimeField("creado", auto_now_add=True)

    class Meta:
        verbose_name = "evento"
        verbose_name_plural = "eventos"
        ordering = ["date", "time"]

    def __str__(self):
        return f"{self.title} ({self.date:%d/%m/%Y})"

    @property
    def day(self):
        return f"{self.date.day:02d}"

    @property
    def month_abbr(self):
        return MESES_ABBR[self.date.month]

    @property
    def color(self):
        return self.COLOR_BY_TAG.get(self.tag, "gold")
