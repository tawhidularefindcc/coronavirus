release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn coresite.wsgi --log-file -
