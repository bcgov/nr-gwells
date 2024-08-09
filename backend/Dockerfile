FROM python:3.6.15-slim-buster AS build

RUN apt-get -y update && apt-get -y install \
    git \
    build-essential \
    gdal-bin \
    libgdal-dev

RUN echo "Checking gdal-config installation"
RUN find / -name gdal-config

ENV PATH="/usr/bin:${PATH}"

WORKDIR /app

RUN python3 -m pip install 'setuptools<58.0'
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install ptvsd

COPY . /app
COPY ./backend-command-script.sh /backend-command-script.sh
COPY ./requirements.txt /requirements.txt

# RUN chmod +x load_fixtures.sh works when i pull the dockerfile into backend but not when dockerfile is with other docker files
RUN chmod +x /app

RUN python3 -m pip install -r requirements.txt

# make script executable
# RUN chmod +x /backend/backend-command-script.sh

# production image step
# FROM python:3.7-slim

# # TODO: need to confirm version of libgdal-dev used with FROM python version
# RUN apt-get -y update && \
#     apt-get -y install libgdal32 \
#     gdal-bin

# ENV PATH="/usr/bin/python3:${PATH}"

# WORKDIR /app

# RUN python3 -m pip install 'setuptools<58.0'
# RUN python3 -m pip install --upgrade pip
# RUN python3 -m pip install ptvsd

# COPY --from=build /app /app
# COPY --from=build /backend-command-script.sh /backend-command-script.sh
# COPY --from=build /requirements.txt /requirements.txt

# RUN chmod +x /app

# RUN python3 -m pip install -r requirements.txt

# make script executable
# RUN chmod +x /backend/backend-command-script.sh

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]