#!/usr/bin/env bash

set -eu

lab_dir=$(mktemp -d "${TMPDIR:-/tmp}/devops-commit-lab.XXXXXX")
cd "$lab_dir"

git init -b main >/dev/null
git config user.name "Nishant Dasgupta"
git config user.email "24bcs10451@localhost"

echo "first line" > tracked.txt
git add tracked.txt
git commit -m "add tracked file" >/dev/null

echo "second line" >> tracked.txt
echo "new file" > untracked.txt
git commit -a -m "update tracked file" >/dev/null

echo "=== AFTER git commit -a -m ==="
git status --short
echo "The new file is not committed."

git add untracked.txt
git commit -m "add untracked file" >/dev/null

echo
echo "=== FINAL LOG ==="
git log --oneline --decorate
echo
echo "Lab folder: $lab_dir"
