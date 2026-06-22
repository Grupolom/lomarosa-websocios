"""Carga datos de demostración alineados con el mockup de Lomarosa.

Uso:  python manage.py seed_demo
Es idempotente: puede ejecutarse varias veces sin duplicar.
"""

import unicodedata
from datetime import date, time

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


def ascii_slug(value):
    """Quita acentos para construir correos (Pérez -> perez)."""
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(c for c in normalized if not unicodedata.combining(c)).lower()

from apps.calendario.models import Event
from apps.core.models import Announcement, Restaurant
from apps.descuentos.models import Coupon, Redemption
from apps.feed.models import Post

User = get_user_model()

PASSWORD = "lomarosa2026"


class Command(BaseCommand):
    help = "Crea datos de demostración del Portal de Socios Lomarosa."

    def handle(self, *args, **options):
        self.stdout.write("Sembrando datos de demostración...")

        # ── Administrador ──
        admin, created = User.objects.get_or_create(
            email="admin@lomarosa.com",
            defaults={
                "first_name": "Admin",
                "last_name": "Lomarosa",
                "role": User.Role.ADMIN,
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if created:
            admin.set_password(PASSWORD)
            admin.save()

        # ── Socios ──
        socios_data = [
            ("Carlos", "Pérez", "CP-0012", 85),
            ("María", "López", "ML-0007", 120),
            ("Jorge", "Rueda", "JR-0021", 60),
            ("Ana", "Torres", "AT-0033", 95),
            ("Pedro", "Gómez", "PG-0045", 40),
        ]
        socios = {}
        for first, last, code, acc in socios_data:
            email = f"{ascii_slug(first)}.{ascii_slug(last)}@lomarosa.com"
            u, c = User.objects.get_or_create(
                email=email,
                defaults={
                    "first_name": first,
                    "last_name": last,
                    "role": User.Role.SOCIO,
                    "socio_code": code,
                    "acciones": acc,
                },
            )
            if c:
                u.set_password(PASSWORD)
                u.save()
            socios[code] = u
        carlos = socios["CP-0012"]

        # ── Anuncio (banner) ──
        Announcement.objects.get_or_create(
            text="Asamblea General de Socios — 6 de Julio.",
            defaults={"link_label": "Confirma tu asistencia", "link_url": "/calendario/"},
        )

        # ── Cupones + canjes ──
        for code, owner in socios.items():
            initials = owner.initials
            coupon, _ = Coupon.objects.get_or_create(
                owner=owner,
                defaults={
                    "code": f"LOMA-{initials}-24",
                    "percent": 15,
                    "valid_until": date(2026, 12, 31),
                    "max_redemptions": 20,
                },
            )
        carlos_coupon = carlos.coupon
        redemptions = [
            ("Carnes La Sabana", date(2026, 6, 1), Redemption.Status.CANJEADO),
            ("Asadero El Palacio", date(2026, 5, 30), Redemption.Status.CANJEADO),
            ("El Corte Bogotá", date(2026, 5, 28), Redemption.Status.CANJEADO),
            ("Casa del Asado", date(2026, 5, 22), Redemption.Status.PENDIENTE),
            ("La Hacienda", date(2026, 5, 20), Redemption.Status.EXPIRADO),
        ]
        if not carlos_coupon.redemptions.exists():
            for est, d, st in redemptions:
                Redemption.objects.create(
                    coupon=carlos_coupon, establishment=est, date=d, status=st
                )

        # ── Eventos ──
        events = [
            {
                "title": "Asamblea General Lomarosa 2026",
                "date": date(2026, 7, 6), "time": time(9, 0),
                "location": "Sala Principal", "platform": Event.Platform.TEAMS,
                "tag": Event.Tag.OBLIGATORIA,
            },
            {
                "title": "Capacitación: Control de Calidad",
                "date": date(2026, 7, 15), "time": time(10, 0),
                "location": "Microsoft Teams", "platform": Event.Platform.TEAMS,
                "tag": Event.Tag.RECOMENDADA,
            },
            {
                "title": "Mesa de Capitalización Q3",
                "date": date(2026, 7, 22), "time": time(15, 0),
                "location": "Zoom", "platform": Event.Platform.ZOOM,
                "tag": Event.Tag.SOLO_SOCIOS,
            },
            {
                "title": "Feria del Ganado — Medellín",
                "date": date(2026, 6, 28), "time": time(8, 0),
                "location": "Plaza Mayor", "platform": Event.Platform.PRESENCIAL,
                "tag": Event.Tag.COMERCIAL,
            },
        ]
        for e in events:
            Event.objects.get_or_create(title=e["title"], date=e["date"], defaults=e)

        # ── Posts ──
        posts = [
            {
                "title": "Resultados de comercialización Q1 2026",
                "category": Post.Category.NOTICIAS, "glyph": "L", "reactions": 24,
                "excerpt": "Volumen récord durante el primer trimestre. Conoce los detalles completos en el informe oficial para socios.",
            },
            {
                "title": "Lomarosa en Bogotá Eats 2026 — un éxito total",
                "category": Post.Category.EVENTO, "glyph": "★", "reactions": 41,
                "excerpt": "Más de 3.000 visitantes en nuestro stand. Comparte el video oficial y ayúdanos a crecer en redes.",
            },
            {
                "title": "Convocatoria Asamblea General — 6 de Julio",
                "category": Post.Category.CIRCULAR, "glyph": "§", "reactions": 30,
                "excerpt": "Se convoca a todos los socios a la Asamblea Ordinaria de mitad de año. Su asistencia es fundamental.",
            },
        ]
        for p in posts:
            Post.objects.get_or_create(
                title=p["title"], defaults={**p, "author": admin}
            )

        # ── Restaurantes / puntos aliados ──
        restos = [
            ("Carnes La Sabana", "Zona Rosa · Bogotá", "🥩", 5, 1),
            ("Asadero El Palacio", "Chapinero · Bogotá", "🍖", 5, 2),
            ("Parrilla Premium", "Usaquén · Bogotá", "🔥", 5, 3),
            ("La Hacienda Grill", "Suba · Bogotá", "🏠", 4, 4),
            ("El Buen Corte", "Teusaquillo · Bogotá", "🌿", 5, 5),
            ("Casa del Asado", "Kennedy · Bogotá", "🎉", 4, 6),
        ]
        for name, zone, emoji, rating, order in restos:
            Restaurant.objects.get_or_create(
                name=name,
                defaults={"zone": zone, "emoji": emoji, "rating": rating, "order": order},
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Listo. Login admin: admin@lomarosa.com  ·  socio: carlos.perez@lomarosa.com  ·  clave: {PASSWORD}"
            )
        )
