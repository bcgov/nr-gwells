FROM node:14.21.3 AS frontend

ENV LOG_LEVEL="info"

RUN apt update && \
    apt install -y git build-essential python3 python3-pip make g++ && \
    apt autoremove -y && \
    apt clean

WORKDIR /app

COPY ./frontend/package*.json ./

RUN npm install

COPY ./frontend/ /app

RUN npm run build

FROM python:3.7

# # Envars
ENV ENVIRONMENT="local"
# ENV CSRF_COOKIE_SECURE="False"
ENV CUSTOM_GDAL_GEOS="False"
# ENV DATABASE_NAME=gwells
# ENV DATABASE_USER="gwells"
# ENV DATABASE_PASSWORD="test1"
# ENV DATABASE_SERVICE_NAME=gwells
# ENV DJANGO_ADMIN_URL=admin
# ENV DJANGO_DEBUG="true"
# ENV DJANGO_SECRET_KEY=secret
# ENV ENABLE_ADDITIONAL_DOCUMENTS="true"
# ENV ENABLE_AQUIFERS_SEARCH="true"
ENV GWELLS_SERVICE_HOST="db"
ENV GWELLS_SERVICE_PORT="5432"
# ENV MINIO_ACCESS_KEY=minio
# ENV MINIO_SECRET_KEY=minio1234
# ENV PYTHONUNBUFFERED="1"
# ENV SESSION_COOKIE_SECURE="False"
# ENV SSO_AUDIENCE=gwells-4121
# ENV SSO_CLIENT=gwells-4121
# ENV SSO_TEST_AUDIENCE=gwells-api-tests-4820
# ENV SSO_TEST_CLIENT=gwells-api-tests-4820
# ENV SSO_AUTH_HOST=https://test.loginproxy.gov.bc.ca/auth
# ENV SSO_IDP_HINT="undefined"
# ENV SSO_PORT=0
# ENV SSO_REALM=standard
# ENV SSO_PUBKEY=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiFdv9GA83uHuy8Eu9yiZHGGF9j6J8t7FkbcpaN81GDjwbjsIJ0OJO9dKRAx6BAtTC4ubJTBJMPvQER5ikOhIeBi4o25fg61jpgsU6oRZHkCXc9gX6mrjMjbsPaf3/bjjYxP5jicBDJQeD1oRa24+tiGggoQ7k6gDEN+cRYqqNpzC/GQbkUPk8YsgroncEgu8ChMh/3ERsLV2zorchMANUq76max16mHrhtWIQxrb/STpSt4JuSlUzzBV/dcXjJe5gywZHe0jAutFhNqjHzHdgyaC4RAd3eYQo+Kl/JOgy2AZrnx+CiPmvOJKe9tAW4k4H087ng8aVE40v4HW/FEbnwIDAQAB
# ENV S3_HOST=minio-public:9000
# ENV S3_PRIVATE_HOST=minio-private:9001
# ENV S3_PRIVATE_BUCKET=gwells
# ENV S3_PRIVATE_ROOT_BUCKET=gwells
# ENV S3_PRIVATE_WELL_BUCKET=well-docs
# ENV S3_PRIVATE_AQUIFER_BUCKET=aquifer-docs
# ENV S3_PRIVATE_REGISTRANT_BUCKET=driller-docs
# ENV S3_PUBLIC_ACCESS_KEY=minio
# ENV S3_PUBLIC_SECRET_KEY=minio1234
# ENV S3_AQUIFER_BUCKET=aquifer-docs
# ENV S3_REGISTRANT_BUCKET=driller-docs
# ENV S3_ROOT_BUCKET=gwells
# ENV S3_WELL_BUCKET=well-docs
# ENV S3_WELL_EXPORT_BUCKET=gwells
# ENV S3_USE_SECURE=0
# ENV EMAIL_NOTIFICATION_RECIPIENT=sustainment.team@gov.bc.ca
ENV GEOCODER_ADDRESS_API_BASE=https://geocoder.api.gov.bc.ca/addresses.json?
# ENV LOCAL="true"
# ENV LOAD_FIXTURES="true"

# Install dependencies
RUN apt -y update && apt -y install git build-essential gdal-bin libgdal-dev

ENV PATH="/usr/bin/python3:${PATH}"

WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install ptvsd
RUN python3 -m pip install 'setuptools<58.0'

COPY ./backend /app
# COPY ./backend-command-script.sh /backend-command-script.sh
COPY ./backend/requirements.txt /app/requirements.txt

COPY --from=frontend ./app/dist ./gwells/static
COPY --from=frontend ./app/dist/index.html ./gwells/templates/

# RUN chmod +x load_fixtures.sh works when i pull the dockerfile into backend but not when dockerfile is with other docker files
RUN chmod +x /app

# RUN python3 -m pip install -r requirements.txt

RUN python3 -m pip install -r requirements.txt

# TODO: move to entrypoint in deployment template?
# chmod -R 777 /app && \
CMD sh -c "python3 manage.py migrate --noinput && \
    ./load_fixtures.sh all && \
    python3 manage.py createinitialrevisions && \
    python3 manage.py collectstatic --noinput && \
    # python3 manage.py export --cleanup=1 --upload=1 && \
    python3 manage.py runserver 0.0.0.0:8000"
