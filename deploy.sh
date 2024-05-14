echo "

Starting deploy build"
echo "___________________________"


echo "
___________________________"
echo "Downloading requirements"
echo "___________________________"
python3 -m pip install -r requirements.txt


echo "
___________________________"
echo "Migrating DB"
echo "___________________________"
python3 manage.py makemigrations
python3 manage.py migrate


echo "
___________________________"
echo "Collecting static files (css, img, js)"
echo "___________________________"
python3 manage.py collectstatic --noinput --clear


echo "
___________________________"
echo "Dealing with unused files (tests, .gitignore, ...)"
echo "___________________________"
find requirements.txt -delete
find LICENSE -delete
find tests/* tests/.* ./*/test*.py test/* -delete


echo "

Ending deploy build"
echo "___________________________"

