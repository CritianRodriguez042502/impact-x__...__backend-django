#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala las dependencias de Python
pip install -r requirements.txt

# Ejecuta las migraciones de la base de datos
python manage.py migrate

# Ejecuta comandos de Python personalizados para crear datos
python manage.py shell <<EOF
from apps.blog.models import Categoryes

software = Categoryes.objects.create(name="Software", slug="slugSoftware")
marketing = Categoryes.objects.create(name="Marketing", slug="slugMarketing")
juegos = Categoryes.objects.create(name="Videojuegos", slug="slugVideojuegos")
ciberseguridad = Categoryes.objects.create(name="Ciberseguridad", slug="slugCiberseguridad")
robotica = Categoryes.objects.create(name="Robotica", slug="slugRobotica")

# Puedes agregar más comandos de creación de datos si es necesario

EOF

# Recoge archivos estáticos
python manage.py collectstatic --no-input
