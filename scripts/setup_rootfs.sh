#!/bin/bash
set -e

ROOTFS=./rootfs

mkdir -p $ROOTFS
docker export $(docker create alpine) | tar -C $ROOTFS -xvf -
