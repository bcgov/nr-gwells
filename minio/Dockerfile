FROM minio/minio:RELEASE.2020-11-25T22-36-25Z

COPY ./minio-entrypoint.sh /

USER 1001

RUN ["chmod", "+x", "/minio-entrypoint.sh"]
ENTRYPOINT /minio-entrypoint.sh

# RUN mkdir -p $MINIO_DATA_DIR/aquifer-docs
# RUN mkdir -p $MINIO_DATA_DIR/driller-docs
# RUN mkdir -p $MINIO_DATA_DIR/gwells
# RUN mkdir -p $MINIO_DATA_DIR/well-docs
# RUN mkdir -p $MINIO_DATA_DIR/gwells-docs