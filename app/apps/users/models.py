from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    """Socio o administrador de Grupolom. Login por correo electrónico."""

    class Role(models.TextChoices):
        ADMIN = "admin", "Administrador"
        SOCIO = "socio", "Socio"

    username = None  # autenticamos por email
    email = models.EmailField("correo electrónico", unique=True)
    role = models.CharField(
        "rol", max_length=10, choices=Role.choices, default=Role.SOCIO
    )
    socio_code = models.CharField(
        "código de socio", max_length=20, blank=True, help_text="Ej: CP-0012"
    )
    acciones = models.PositiveIntegerField("acciones", default=0)
    phone = models.CharField("teléfono", max_length=30, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return self.get_full_name() or self.email

    @property
    def is_admin_role(self):
        return self.role == self.Role.ADMIN

    @property
    def initials(self):
        parts = [self.first_name, self.last_name]
        ini = "".join(p[0] for p in parts if p)
        return (ini or self.email[:2]).upper()
