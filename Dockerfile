FROM public.ecr.aws/docker/library/python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir newrelic

COPY . .
# Asegúrate de incluir `newrelic.ini` en el contexto o copiarlo explícitamente
COPY newrelic.ini /app/newrelic.ini
RUN chmod +x /app/entrypoint.sh


ENV NEW_RELIC_APP_NAME="devops-app-v2"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LICENSE_KEY=86894dbadbc875ec8b6e6b34510d4e76FFFFNRAL
ENV NEW_RELIC_LOG_LEVEL=info

EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["/bin/bash", "-c", "python run.py"]