web: python app/manage.py migrate --noinput && python app/manage.py collectstatic --noinput && gunicorn --chdir app config.wsgi --bind 0.0.0.0:$PORT
