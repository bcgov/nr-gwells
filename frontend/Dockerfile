FROM node:14.21.3 AS build

ENV LOG_LEVEL="info"

RUN apt-get update && \
    apt-get install -y git build-essential python3 python3-pip make g++ && \
    apt-get autoremove -y && \
    apt-get clean

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . /app

RUN npm run build

# FROM caddy:2.8.1

# # Copy static files, verify Caddyfile formatting
# COPY --from=build /app/dist /srv/gwells
# COPY Caddyfile /etc/caddy/Caddyfile
# RUN caddy fmt /etc/caddy/Caddyfile

# # Nonroot user
# # USER 1001

# # CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile"]

# # FROM node:14.21.3

# # COPY --from=build /app /app

# # CMD ["npm" "run" "serve"]

# Deploy using Caddy to host static files
FROM caddy:2.8.4-alpine
RUN apk add --no-cache ca-certificates

# Copy static files, verify Caddyfile formatting
COPY --from=build /app/dist /srv/gwells
COPY Caddyfile /etc/caddy/Caddyfile
RUN caddy fmt /etc/caddy/Caddyfile

# Boilerplate, not used in OpenShift/Kubernetes
EXPOSE 3005 3001
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:3001/health

# Nonroot user
USER 1001
