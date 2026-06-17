# Tarea actual

## En progreso: Setup inicial del proyecto

**Fecha:** 17 de junio de 2026
**Fase:** 0 — Setup y configuración base

### Completado

- [x] Crear `requirements.txt` con dependencias base
- [x] Instalar dependencias en venv
- [x] Crear proyecto Django con `manage.py` y `config/`
- [x] Crear carpeta `app/` y mover todo Django ahí (`config/`, `apps/`, `templates/`, `static/`, `manage.py`)
- [x] Crear carpetas vacías para las 6 apps dentro de `app/apps/`
- [x] Crear `CLAUDE.md`, `README.md`, `progress/`

### Pendiente completar

- [ ] Correr `py manage.py startapp` para las 6 apps (users, feed, archivos, calendario, descuentos, core)
- [ ] Separar `config/settings.py` en `base.py`, `development.py`, `production.py`
- [ ] Crear `.env` y `.env.example`
- [ ] Crear `Procfile` y `runtime.txt` para Railway
- [ ] Configurar `INSTALLED_APPS` con las 6 apps
- [ ] Primera migración y verificar `py manage.py runserver`

### Siguiente tarea

App `users` — modelo User extendido con roles Admin/Socio
