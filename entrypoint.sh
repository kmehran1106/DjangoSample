#!/bin/bash

python manage.py migrate --no-input || exit 1
python manage.py collectstatic --no-input --clear

exec "$@"