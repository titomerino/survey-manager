web: gunicorn studentsurvey.wsgi --log-file -

web: python manage.py migrate && gunicorn studentsurvey.wsgi