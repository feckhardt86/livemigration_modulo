release: python manage.py migrate && python manage.py loaddata initial_data
web: gunicorn openstack.wsgi --log-file -
