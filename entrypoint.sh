set -e

NEWRELIC_INI="/app/newrelic.ini"

if [ -z "$NEW_RELIC_LICENSE_KEY" ]; then
  echo "WARNING: NEW_RELIC_LICENSE_KEY no está configurada"
fi

if [ ! -f "$NEWRELIC_INI" ]; then
  echo "ERROR: no se encontró $NEWRELIC_INI"
  exit 1
fi

# Si no se pasa comando, usar el CMD por defecto
if [ $# -eq 0 ]; then
  set -- python run.py
fi

exec newrelic-admin run-program "$@"