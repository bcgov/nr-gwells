FROM node:14.21.3 AS build

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python3 \
    python3-pip \
    make \
    g++

WORKDIR /app

COPY package*.json ./

RUN npm i

COPY . /app

RUN npm run build

FROM node:14.21.3

COPY --from=build /app /app

CMD ["npm" "run" "serve"]