FROM crunchydata/crunchy-postgres-gis:centos7-12.2-4.2.2

# Copy startup scripts
COPY /* /docker-entrypoint-initdb.d/

# User, port and Healthcheck
USER postgres
EXPOSE 5432
HEALTHCHECK --interval=5s --timeout=5s --retries=5 CMD [ "pg_isready", "-U", "postgres"]