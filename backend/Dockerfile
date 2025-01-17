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

# Install dependencies
RUN apt -y update && apt -y install git build-essential gdal-bin libgdal-dev postgresql-client

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
# COPY /backend/startup.sh /docker-entrypoint-initdb.d/

# RUN chmod +x load_fixtures.sh works when i pull the dockerfile into backend but not when dockerfile is with other docker files
RUN chmod -R +x /app
# RUN chmod -R 777 /app 
# RUN python3 -m pip install -r requirements.txt

RUN python3 -m pip install -r requirements.txt

# TODO: move to entrypoint in deployment template?
# chmod -R 777 /app && \
# CMD [""]

CMD sh -c "python3 manage.py migrate --noinput && \
    ./load_fixtures.sh all && \
    python3 manage.py createinitialrevisions && \
    python3 manage.py collectstatic --noinput && \
    # python3 manage.py export --cleanup=1 --upload=1 && \
    python3 manage.py runserver 0.0.0.0:8000"

USER 1001