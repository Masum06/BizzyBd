echo Starting Gunicorn.
exec gunicorn bizzybd.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
