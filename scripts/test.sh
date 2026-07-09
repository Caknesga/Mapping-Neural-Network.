#!/bin/bash
set -e 


SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# Resolve parent directory (one level above repo)
PARENT_DIR="$(cd "$REPO_DIR/.." && pwd)"

cd "$PARENT_DIR"

echo "test" > test.txt

source cadence_intel16.sh