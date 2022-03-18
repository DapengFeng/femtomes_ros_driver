#!/bin/bash -e

set -v

echo "Running isort ..."
isort --atomic -y

echo "Running black ..."
black -l 80 .

echo "Running flake8 ..."
flake8 .