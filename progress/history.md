# Historial de cambios

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
