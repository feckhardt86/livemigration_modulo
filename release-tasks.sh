#!/usr/bin/env bash

python manage.py migrate
python manage.py loaddata initial_data