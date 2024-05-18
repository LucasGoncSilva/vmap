# Enters project's dir
cd VMAP

# Sets to exit on error
set -o errexit

# Installs dependencies
pip install -r requirements.txt

# Collects staticfiles
python manage.py collectstatic --no-input

# Handles DB migrations
python manage.py makemigrations
python manage.py migrate
