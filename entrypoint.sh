#!/bin/sh
set -e

if [ x"$DO_DJANGO_INIT" != x ]; then
  python manage.py migrate --skip-checks
  python manage.py collectstatic --no-input
fi

exec "$@"