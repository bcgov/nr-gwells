FROM node:14.21.3 AS build

RUN apt-get update

RUN apt-get install -y git build-essential python3 python3-pip make g++

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . /app

RUN npm run build

FROM caddy:alpine

COPY --from=build /app/dist /usr/share/caddy

# CMD run sh -c "npm run serve"

# FROM node:14.21.3

# COPY --from=build /app /app

# CMD ["npm" "run" "serve"]