# FROM node:14.21.3 AS build
FROM node:14.21.3

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

CMD run sh -c "npm run serve"

# FROM node:14.21.3

# COPY --from=build /app /app

# CMD ["npm" "run" "serve"]