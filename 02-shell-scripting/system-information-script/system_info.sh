#!/usr/bin/env bash

set -u

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
report_dir="$script_dir/system-report"
process_file="$report_dir/process.log"

read -r -p "Enter your name: " name
read -r -p "Enter a short note: " note

current_date=$(date)
host_name=$(hostname)
user_name=$(whoami)

mkdir -p "$report_dir"
touch "$process_file"
ps aux > "$process_file"

echo
echo "Name: $name"
echo "Note: $note"
echo "Date: $current_date"
echo "Host: $host_name"
echo "User: $user_name"
echo
echo "Disk use:"
df -h
echo
echo "Running processes (first 10 lines):"
head -n 10 "$process_file"
echo
echo "Process list saved to: $process_file"
