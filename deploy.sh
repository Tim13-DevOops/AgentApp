#!/bin/bash

echo "START"
VERSION=${1}
HEROKU_EMAIL=${2}
HEROKU_API_KEY=${3}
TERRAFORM_PG_BACKEND=${4}
SQL_PASSWORD=${5}
FLASK_SECRET_KEY=${6}
SQL_DB_NAME=${7}
SQL_USERNAME=${8}
JWT_SECRET_KEY=${9}

STAGE=${10-stage}
DOCKERHUB_USERNAME=${11:-dusanpanda}
CONTAINER_NAME=${12:-terraform-deploy}

FLASK_APP=project/__init__.py
FLASK_ENV=development
SQL_HOST=ella.db.elephantsql.com
SQL_PORT=5432
DATABASE=postgres
COMMAND=run_server
POSTGRES_PASSWORD=${SQL_PASSWORD}
POSTGRES_USER=${SQL_USERNAME}
POSTGRES_DB=${SQL_DB_NAME}
DEBUG_METRICS=False

BACKEND_IMAGE=${DOCKERHUB_USERNAME}/agent_backend:${VERSION}

docker create \
  --workdir /deployment \
  --entrypoint sh \
  --env HEROKU_API_KEY="${HEROKU_API_KEY}" \
  --env HEROKU_EMAIL="${HEROKU_EMAIL}" \
  --env TERRAFORM_PG_BACKEND="${TERRAFORM_PG_BACKEND}" \
  --env STAGE="${STAGE}" \
  --env BACKEND_IMAGE="${BACKEND_IMAGE}" \
  --env FLASK_APP="${FLASK_APP}" \
  --env FLASK_ENV="${FLASK_ENV}" \
  --env FLASK_SECRET_KEY="${FLASK_SECRET_KEY}" \
  --env SQL_HOST="${SQL_HOST}" \
  --env SQL_PASSWORD="${SQL_PASSWORD}" \
  --env SQL_PORT="${SQL_PORT}" \
  --env SQL_DB_NAME="${SQL_DB_NAME}" \
  --env SQL_USERNAME="${SQL_USERNAME}" \
  --env DATABASE="${DATABASE}" \
  --env COMMAND="${COMMAND}" \
  --env POSTGRES_PASSWORD="${POSTGRES_PASSWORD}" \
  --env POSTGRES_USER="${POSTGRES_USER}" \
  --env POSTGRES_DB="${POSTGRES_DB}" \
  --env JWT_SECRET_KEY="${JWT_SECRET_KEY}" \
  --env DEBUG_METRICS="${DEBUG_METRICS}" \
  --name "${CONTAINER_NAME}" \
  danijelradakovic/heroku-terraform \
  deploy.sh

docker cp deployment/. "${CONTAINER_NAME}":/deployment/
docker start -i "${CONTAINER_NAME}"
docker rm "${CONTAINER_NAME}"