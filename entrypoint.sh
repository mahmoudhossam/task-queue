#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

export DATABASE_URL="postgres://user:password@postgres:5432/users"

postgres_ready() {
python << END
import sys

import psycopg2

try:
    psycopg2.connect(
        dbname="postgres",
        user="user",
        password="password",
        host="postgres",
        port="5432",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'

python db.py

exec "$@"
