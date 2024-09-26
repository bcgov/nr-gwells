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

RUN echo "npm install"
RUN npm install

COPY . /app

RUN npm run build

RUN echo "CMD to run"
CMD run sh -c "echo 'Dockerfile Command' && \
    npm run serve"

# FROM node:14.21.3

# COPY --from=build /app /app

# CMD ["npm" "run" "serve"]