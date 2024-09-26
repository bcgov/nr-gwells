FROM node:14.21.3 AS build

RUN apt-get update

RUN apt-get install -y git build-essential python3 python3-pip make g++

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . /app

RUN npm run build

FROM caddy:2

# Copy static files, verify Caddyfile formatting
COPY --from=build /app/dist /srv
COPY Caddyfile /etc/caddy/Caddyfile
RUN caddy fmt /etc/caddy/Caddyfile

# FROM node:14.21.3

# COPY --from=build /app /app

# CMD ["npm" "run" "serve"]