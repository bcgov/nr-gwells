#!/bin/sh
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

set -x

mkdir -p $MINIO_DATA_DIR/aquifer-docs
mkdir -p $MINIO_DATA_DIR/driller-docs
mkdir -p $MINIO_DATA_DIR/gwells
mkdir -p $MINIO_DATA_DIR/well-docs
mkdir -p $MINIO_DATA_DIR/gwells-docs

/usr/bin/docker-entrypoint.sh $@
