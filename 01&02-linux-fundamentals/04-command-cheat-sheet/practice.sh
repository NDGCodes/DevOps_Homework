#!/usr/bin/env bash

set -u

echo "=== DATE ==="
date

echo "=== HOSTNAME ==="
hostname

echo "=== USER ==="
whoami

echo "=== CURRENT FOLDER ==="
pwd

echo "=== SYSTEM ==="
uname -a

echo "=== DISK ==="
df -h

echo "=== MEMORY ==="
free -h

echo "=== PROCESSES ==="
ps aux
