#!/usr/bin/env bash

set -u

echo "=== IP ADDRESS ==="
ip -brief addr

echo "=== ROUTE ==="
ip route

echo "=== PING ==="
ping -c 2 127.0.0.1

echo "=== DNS ==="
getent hosts example.com

echo "=== OPEN PORTS ==="
ss -tuln

echo "=== HTTP HEADERS ==="
curl -I --max-time 10 https://example.com
