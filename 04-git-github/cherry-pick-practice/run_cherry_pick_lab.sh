#!/usr/bin/env bash

set -eu

lab_dir=$(mktemp -d "${TMPDIR:-/tmp}/devops-cherry-pick-lab.XXXXXX")
cd "$lab_dir"

git init -b main >/dev/null
git config user.name "Nishant Dasgupta"
git config user.email "24bcs10451@localhost"

echo "base" > app.txt
git add app.txt
git commit -m "add app" >/dev/null

echo "main change" >> app.txt
git commit -a -m "update app on main" >/dev/null

echo "notes" > notes.txt
git add notes.txt
git commit -m "add notes on main" >/dev/null

git switch -c feature >/dev/null

echo "feature one" > feature-one.txt
git add feature-one.txt
git commit -m "add feature one" >/dev/null

echo "picked feature" > picked-feature.txt
git add picked-feature.txt
git commit -m "add picked feature" >/dev/null
picked_commit=$(git rev-parse HEAD)

echo "feature three" > feature-three.txt
git add feature-three.txt
git commit -m "add feature three" >/dev/null

git switch main >/dev/null
git cherry-pick "$picked_commit" >/dev/null

echo "=== PICKED COMMIT ==="
echo "$picked_commit"
echo
echo "=== ALL BRANCHES ==="
git log --oneline --graph --decorate --all
echo
echo "=== FILE ON MAIN ==="
cat picked-feature.txt
echo
echo "Lab folder: $lab_dir"
