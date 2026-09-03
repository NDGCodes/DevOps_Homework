#!/usr/bin/env bash

set -eu

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

docker run --rm \
  -v "$script_dir:/work" \
  -w /work \
  ubuntu:24.04 \
  bash -c 'apt-get update >/dev/null && DEBIAN_FRONTEND=noninteractive apt-get install -y iproute2 iputils-ping curl >/dev/null && ./network_check.sh'
