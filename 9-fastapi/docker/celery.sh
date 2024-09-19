#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  celery --app=src.documents.tasks:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery --app=src.documents.tasks:celery flower
fi