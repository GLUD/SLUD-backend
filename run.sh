#!/bin/sh

SECRET_KEY=${SECRET_KEY:-}
ADMIN_USER=${ADMIN_USER:-'root'}
ADMIN_PASSWORD=${ADMIN_PASSWORD:-}
ADMIN_PASSWORD_FILE=${ADMIN_PASSWORD_FILE:-}
ADMIN_EMAIL=${ADMIN_EMAIL:-}

if [ ! -z "$ADMIN_PASSWORD_FILE" ]; then ADMIN_PASSWORD=$(tail -n 1 "$ADMIN_PASSWORD_FILE"); fi

if [ -z "$ADMIN_PASSWORD" ]; then echo "Bad admin password, set ADMIN_PASSWORD or ADMIN_PASSWORD_FILE"; exit 1; fi

if [ -z "$ADMIN_EMAIL" ]; then echo "Bad admin email, set ADMIN_EMAIL"; exit 1; fi

mkdir -p data


if ! [ -e data/db.sqlite3 ]; then

	# Aplica migraciones
	python manage.py makemigrations
	python manage.py migrate
fi

# crea el directorio de archivos staticos
python manage.py collectstatic


# Crea el superusuario (forma no interactiva de python manage.py createsuperuser)
echo "from django.contrib.auth.models import User; User.objects.filter(email='$ADMIN_EMAIL').delete(); User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')" | python manage.py shell

python manage.py runserver 0.0.0.0:8000
