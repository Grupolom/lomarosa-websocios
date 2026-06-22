# Historial de cambios

---

## 20 de junio de 2026

### Backend completo + integración del diseño (Fases 1, 2 y 4)
- **Configuración de producción**: reescrito `config/settings.py` (dotenv, `dj-database-url`,
  WhiteNoise, custom user, login por email, `es-co`/`America/Bogota`, cookies seguras en prod).
- **App `users`**: modelo `User` personalizado con login por email, roles Admin/Socio,
  `socio_code`, `acciones`; manager propio; admin de Django configurado.
- **App `feed`**: modelos `Post` (categoría, imagen, PDF, reacciones) y `Proposal`; feed,
  reacciones y formulario de participación; admin CRUD.
- **App `calendario`**: modelo `Event` (fecha, hora, plataforma Meet/Teams/Zoom, tipo, enlace);
  vista con grilla mensual navegable + próximos eventos.
- **App `archivos`**: modelo `Document` (solo lectura para el socio; gestión por admin).
- **App `descuentos`**: modelos `Coupon` y `Redemption`; vista de cupón + historial de canjes.
- **App `core`**: dashboard, aliados (`Restaurant`), reuniones, panel admin, `Announcement`;
  context processor para el sidebar; comando `seed_demo` con datos de demostración.
- **Diseño**: HTML del deploy de Railway convertido en `templates/base.html` (sidebar dinámico
  por rol, topbar, modal PDF, toasts desde `messages`) + `static/css/portal.css`; login real;
  plantillas por sección (dashboard, feed, calendario, archivos, cupón, aliados, reuniones, panel).
- **Despliegue**: `requirements.txt` ampliado, `Procfile`, `runtime.txt` (py 3.12), `.env.example`.
- **Corregido**: `apps.py` usaban `name='users'` (incorrecto) → `name='apps.users'` con `label`;
  `archivos/apps.py` traía `FeedConfig` por error del scaffold; emails del seed con acento.
- **Verificado en local**: `check` sin errores, migraciones aplicadas, login por rol, las 8
  secciones renderizan con datos reales y control de acceso admin/socio funcionando (0 errores 500).

---

## 17 de junio de 2026

### Reorganización de estructura
- Creada carpeta `app/` para aislar todo lo de Django
- Movidos `manage.py`, `config/` y `apps/` dentro de `app/`
- Creadas carpetas `app/templates/`, `app/static/css`, `app/static/js`, `app/static/img`
- Creadas carpetas vacías para las 6 apps en `app/apps/` (users, feed, archivos, calendario, descuentos, core)
- Actualizado `CLAUDE.md` con nueva estructura y Procfile con `--chdir app`
- Creado `README.md` con título, descripción y módulos

---

## 16 de junio de 2026

### Setup inicial
- Definido stack: Django 5.1 + HTMX + PostgreSQL (Railway) + Cloudflare R2
- Creado `requirements.txt` con dependencias base
- Instaladas dependencias vía `py -m pip install -r requirements.txt`
- Creado proyecto Django con `py -m django startproject config .`
- Generada estructura base: `config/` con `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`
- Creado `CLAUDE.md` con documentación del proyecto
- Creada carpeta `progress/` con `current.md` e `history.md`
