#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala las dependencias de Python
pip install -r requirements.txt

# Ejecuta las migraciones de la base de datos
python manage.py migrate

# Recoge archivos estáticos
python manage.py collectstatic --no-input
