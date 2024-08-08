FROM python:3.7-slim AS build

RUN apt-get -y update && apt-get -y install git build-essential libgdal-dev && apt-get -y install apt-utils

ENV PATH="/usr/bin/python3:${PATH}"

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
FROM python:3.7-slim

# TODO: need to confirm version of libgdal-dev used with FROM python version
RUN apt-get -y update && \
    apt-get -y install libgdal32

ENV PATH="/usr/bin/python3:${PATH}"

WORKDIR /app

COPY --from=build /app /app
COPY --from=build /backend-command-script.sh /backend-command-script.sh
COPY --from=build /requirements.txt /requirements.txt

RUN chmod +x /app

# make script executable
# RUN chmod +x /backend/backend-command-script.sh

CMD ["/backend-command-script.sh"]