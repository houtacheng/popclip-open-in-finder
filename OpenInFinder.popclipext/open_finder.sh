#!/bin/bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
exec /usr/bin/python3 "$DIR/open_finder.py"
