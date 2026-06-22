from django.conf import settings
from django.db import models


class Coupon(models.Model):
    """Cupón único por socio (DC-01)."""

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="coupon",
        verbose_name="socio",
    )
    code = models.CharField("código", max_length=30, unique=True)
    percent = models.PositiveSmallIntegerField("porcentaje", default=15)
    where = models.CharField(
        "válido en",
        max_length=200,
        default="En carnicerías y puntos aliados Lomarosa",
    )
    valid_until = models.DateField("válido hasta", null=True, blank=True)
    max_redemptions = models.PositiveIntegerField("canjes máximos", default=20)
    active = models.BooleanField("activo", default=True)

    class Meta:
        verbose_name = "cupón"
        verbose_name_plural = "cupones"
        ordering = ["code"]

    def __str__(self):
        return self.code

    @property
    def redeemed_count(self):
        return self.redemptions.filter(status=Redemption.Status.CANJEADO).count()

    @property
    def usage_pct(self):
        if not self.max_redemptions:
            return 0
        return round(self.redeemed_count / self.max_redemptions * 100)


class Redemption(models.Model):
    """Registro de canje de un cupón (DC-04, DC-05)."""

    class Status(models.TextChoices):
        CANJEADO = "canjeado", "Canjeado"
        PENDIENTE = "pendiente", "Pendiente"
        EXPIRADO = "expirado", "Expirado"

    coupon = models.ForeignKey(
        Coupon,
        on_delete=models.CASCADE,
        related_name="redemptions",
        verbose_name="cupón",
    )
    establishment = models.CharField("establecimiento", max_length=200)
    date = models.DateField("fecha")
    status = models.CharField(
        "estado", max_length=10, choices=Status.choices, default=Status.CANJEADO
    )

    class Meta:
        verbose_name = "canje"
        verbose_name_plural = "canjes"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.coupon.code} · {self.establishment}"
