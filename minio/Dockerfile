FROM minio/minio:RELEASE.2020-11-25T22-36-25Z

COPY ./minio-entrypoint.sh /
ENTRYPOINT /minio-entrypoint.sh

RUN sed -i '1 a set -x' /usr/bin/docker-entrypoint.sh 
