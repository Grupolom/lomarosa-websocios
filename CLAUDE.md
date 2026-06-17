# CLAUDE.md — lomarosa-websocios

## Instrucciones para Claude

Al iniciar cualquier conversación en este proyecto:

1. **Leer `progress/current.md`** — contiene la tarea en curso y los pendientes activos.
2. **Leer `progress/history.md`** — contiene el historial de cambios realizados.
3. Al completar cualquier cambio:
   - Mover lo completado de `current.md` a `history.md` (con fecha)
   - Actualizar `current.md` con la nueva tarea o pendientes restantes

---

## Descripción del proyecto

Portal web privado para los 44 socios de Grupolom. Plataforma interna que centraliza comunicación, documentación y beneficios del grupo.

**Deadline duro:** 29 de junio de 2026 (Asamblea general: 6 de julio de 2026)
**Hito crítico:** 20 de junio — Feed de Noticias y Calendario deben estar en producción

---

## Stack

| Capa | Tecnología |
|------|-----------|
| Backend + Frontend | Django 5.1 + Django Templates + HTMX |
| Base de datos | PostgreSQL (Railway plugin) |
| Archivos / PDFs | Cloudflare R2 (S3-compatible) |
| Auth | Django Auth nativo (roles Admin / Socio) |
| Servidor | Gunicorn |
| Deploy | Railway |
| Assets estáticos | Whitenoise |

---

## Estructura del proyecto

```
lomarosa-websocios/
├── app/                         # Todo lo de Django
│   ├── config/                  # Settings, urls raíz, wsgi
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── users/               # Auth, roles Admin/Socio, perfiles
│   │   ├── feed/                # Posts, noticias, visor PDF inline
│   │   ├── archivos/            # Carpetas personales por socio
│   │   ├── calendario/          # Reuniones + botón Meet/Teams
│   │   ├── descuentos/          # Cupones únicos + seguimiento + CRM Samuel
│   │   └── core/                # About, restaurantes, home
│   ├── templates/               # base.html + templates por app
│   ├── static/                  # CSS, JS (HTMX, PDF.js), imágenes
│   └── manage.py
├── progress/                    # Seguimiento de avance del proyecto
├── CLAUDE.md
├── README.md
├── requirements.txt
├── Procfile
└── .env
```

---

## Apps y responsabilidades

- **users** — User extendido con rol (admin/socio), login, logout, perfil editable, recuperación de contraseña
- **feed** — Posts con texto/imagen/PDF, visor inline, panel admin para CRUD de posts
- **archivos** — Carpeta personal por socio, PDFs servidos via URL firmada R2, sin descarga
- **calendario** — Eventos con fecha/tipo/link Meet-Teams, admin CRUD, visible para todos los socios
- **descuentos** — Cupón único por socio, activación por email, dashboard redenciones, integración API CRM Samuel
- **core** — Home, about, restaurantes asociados, banner recordatorio marketing

---

## Variables de entorno requeridas (.env)

```
SECRET_KEY=
DEBUG=True                     # False en producción
DATABASE_URL=                  # Railway lo inyecta automáticamente
R2_ACCOUNT_ID=
R2_ACCESS_KEY_ID=
R2_SECRET_ACCESS_KEY=
R2_BUCKET_NAME=
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=587
```

---

## Comandos útiles

```bash
# Desarrollo local
python manage.py runserver

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Colectar estáticos (producción)
python manage.py collectstatic
```

---

## PDFs — flujo importante

Los PDFs nunca se exponen con URL directa de R2. Siempre pasan por una view de Django que:
1. Verifica autenticación y que el archivo pertenece al socio
2. Genera una URL firmada de R2 con expiración de 5 minutos
3. Devuelve el PDF con `Content-Disposition: inline` (no attachment)
4. El frontend renderiza con PDF.js con toolbar de descarga desactivada

---

## Módulos por prioridad

| Prioridad | App | Fecha objetivo |
|-----------|-----|---------------|
| 1 | users | 17 jun |
| 2 | feed | 19 jun |
| 3 | calendario | 20 jun — HITO |
| 4 | archivos | 22 jun |
| 5 | descuentos | 25 jun |
| 6 | core | 27 jun |
| 7 | QA + deploy | 29 jun |

---

## Dependencias externas

- **CRM Samuel** — API REST para módulo de descuentos. Coordinar endpoints antes del 20 jun.
- **Dominio LOM** — Gestionar DNS desde el inicio del deploy en Railway.

---

## Deploy en Railway

El proyecto usa dos servicios en Railway:
1. **Web** — Django app (`Procfile`: `web: gunicorn config.wsgi`)
2. **PostgreSQL** — Plugin nativo de Railway (inyecta `DATABASE_URL` automáticamente)

`runtime.txt` debe especificar la versión de Python: `python-3.11.x`

El `Procfile` usa `--chdir` porque `manage.py` está dentro de `app/`:
```
web: gunicorn --chdir app config.wsgi
```
