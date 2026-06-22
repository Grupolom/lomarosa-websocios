# Tarea actual

## En progreso: Pulido del MVP y despliegue a Railway

**Fecha:** 20 de junio de 2026
**Fase:** entre Fase 1–4 (estructura + Feed + Calendario listos en local)

### Estado
El backend Django ya está montado y funcionando en local (SQLite). El diseño del
mockup de Railway se integró como `base.html` + `static/css/portal.css` y todas las
secciones renderizan con datos reales.

### Pendiente inmediato (para cumplir el HITO 20 jun en producción)
- [ ] Crear servicio web + plugin PostgreSQL en Railway (proyecto `lomarosa-portal`)
- [ ] Configurar variables: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `DATABASE_URL` (auto)
- [ ] Primer deploy con `Procfile` (migrate + collectstatic + gunicorn)
- [ ] Ejecutar `seed_demo` o cargar los 44 socios reales (AU-04)
- [ ] Verificar Feed y Calendario accesibles para los socios

### Pendiente de módulos (siguientes fases)
- [ ] Feed: subida real de imagen/PDF en posts + visor PDF.js inline (NT-02, NT-06)
- [ ] Archivos: almacenamiento Cloudflare R2 con URL firmada (AR-02/03)
- [ ] Descuentos: envío real de cupón por email + integración CRM Samuel (DC-03, DC-06)
- [ ] Capitalización (Área interna admin) — CI-01..05 (aún sin app)
- [ ] Recuperación de contraseña: configurar backend de email (AU-05)
- [ ] About editable por admin (IN-03)

### Cómo correr en local
```
.venv\Scripts\python app\manage.py runserver
# Login admin:  admin@lomarosa.com        / lomarosa2026
# Login socio:  carlos.perez@lomarosa.com / lomarosa2026
```
