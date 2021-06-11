#!/bin/sh
# wait-for-postgres.sh
  

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 2
    done

    echo "PostgreSQL started"
fi

coverage run setup.py test
coverage xml --include="app/*" -o coverage_reports/coverage.xml

# python setup.py install
# start_server

exec "$@"

