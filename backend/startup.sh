python3 manage.py migrate --noinput &&
./load_fixtures.sh all &&
python3 manage.py createinitialrevisions &&
python3 manage.py collectstatic --noinput &&
# python3 manage.py export --cleanup=1 --upload=1 &&
python3 manage.py runserver 0.0.0.0:8000"
