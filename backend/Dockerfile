# FROM python:3.6.15-slim-buster AS build

# RUN apt-get -y update && apt-get -y install \
#     git \
#     build-essential \
#     gdal-bin \
#     libgdal-dev

# RUN echo "Checking gdal-config installation"
# RUN find / -name gdal-config

# ENV PATH="/usr/bin:${PATH}"

# WORKDIR /app

# RUN python3 -m pip install 'setuptools<58.0'
# RUN python3 -m pip install --upgrade pip
# RUN python3 -m pip install ptvsd

# COPY . /app
# COPY ./backend-command-script.sh /backend-command-script.sh
# COPY ./requirements.txt /requirements.txt

# # RUN chmod +x load_fixtures.sh works when i pull the dockerfile into backend but not when dockerfile is with other docker files
# RUN chmod +x /app

# RUN python3 -m pip install -r requirements.txt

# # make script executable
# # RUN chmod +x /backend/backend-command-script.sh

# # production image step
# # FROM python:3.7-slim

# # # TODO: need to confirm version of libgdal-dev used with FROM python version
# # RUN apt-get -y update && \
# #     apt-get -y install libgdal32 \
# #     gdal-bin

# # ENV PATH="/usr/bin/python3:${PATH}"

# # WORKDIR /app

# # RUN python3 -m pip install 'setuptools<58.0'
# # RUN python3 -m pip install --upgrade pip
# # RUN python3 -m pip install ptvsd

# # COPY --from=build /app /app
# # COPY --from=build /backend-command-script.sh /backend-command-script.sh
# # COPY --from=build /requirements.txt /requirements.txt

# # RUN chmod +x /app

# # RUN python3 -m pip install -r requirements.txt

# # make script executable
# # RUN chmod +x /backend/backend-command-script.sh

# # CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


FROM registry.access.redhat.com/rhscl/python-36-rhel7:1


# Switch to root user
#
USER root


# External libraries required by Python GIS extensions (e.g. GeoDjango, GeoAlchemy)
# Install and configure GEOS
#
# Note: HTTPS will result in certificate errors, hence the downgrade to HTTP here
#

RUN cd /tmp && wget http://download.osgeo.org/geos/geos-3.7.1.tar.bz2 && \
    tar xjf geos-3.7.1.tar.bz2 && \
    cd geos-3.7.1/ && \
    ./configure --prefix=/usr/local && \
    make && \
    make install && \
    ldconfig && \
    cd /tmp && \
    rm -rf /tmp/geos-3.7.1 /tmp/geos-3.7.1.tar.bz2


# Install and configure PROJ.4
#
# Note: HTTPS will result in certificate errors, hence the downgrade to HTTP here
#

RUN cd /tmp && wget http://download.osgeo.org/proj/proj-5.2.0.tar.gz && \
    wget http://download.osgeo.org/proj/proj-datumgrid-north-america-1.1.tar.gz && \
    tar xzf proj-5.2.0.tar.gz && \
    cd proj-5.2.0/nad && \
    tar xzf ../../proj-datumgrid-north-america-1.1.tar.gz && \
    cd .. && \
    ./configure --prefix=/usr/local && \
    make \
    && make install && \
    ldconfig && \
    rm -rf /tmp/proj-5.2.0 /tmp/proj-5.2.0.tar.gz /tmp/proj-datumgrid-north-america-1.1.tar.gz


# Install and configure GDAL
# (without SFCGAL as we aren't using "CREATE EXTENSION postgis_sfcgal;")
#

RUN cd /tmp && wget http://download.osgeo.org/gdal/2.4.0/gdal-2.4.0.tar.gz && \
    tar zxvf gdal-2.4.0.tar.gz && cd gdal-2.4.0/ && \
    ./configure --prefix=/usr/local --with-python --with-sfcgal=no && \
    make -j4 && \
    make install && \
    ldconfig && \
    rm -rf /tmp/gdal-2.4.0 /tmp/gdal-2.4.0.tar.gz


# Configure GDAL file locations
#
RUN echo "/usr/local/lib/" >> /etc/ld.so.conf && \
    ldconfig


USER 1001
