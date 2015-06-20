#!/bin/bash
# Invoke like $ ./startup.sh <env_name>
# e.x:  $ ./startup.sh production
export DJANGO_SETTINGS_MODULE=settings.$1
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$(dirname $DIR)"
source $ROOT/env/pyvenv/bin/activate
PYTHONPATH=$ROOT/djangoapp gunicorn -c $ROOT/conf/gunicorn.$1.conf project.wsgi:application $2
