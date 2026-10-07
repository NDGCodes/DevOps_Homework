#!/usr/bin/env bash

set -eu

docker run --rm ubuntu:24.04 bash -c '
  apt-get update >/dev/null
  DEBIAN_FRONTEND=noninteractive apt-get install -y adduser >/dev/null
  adduser --disabled-password --gecos "" devops_test
  id devops_test
  getent passwd devops_test
'
