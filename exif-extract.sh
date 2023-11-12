#!/bin/bash
DIRNAME=`realpath $(dirname $0)`
pushd $DIRNAME/sources
exiftool -j *.jpg > $DIRNAME/index.json
popd
