#!/bin/bash

# Configuration
VENV=${1:-.venv}
ENVIRONMENT=${2:-local}

# Create venv if it doesn't exist
if [ ! -d ${VENV} ]; then
    echo "Creating ${VENV}"
    if command -v uv >/dev/null 2>&1; then
        echo "Using uv"
        uv venv ${VENV}
    else
        echo "uv not installed. Using python"
        python3 -m venv ${VENV}
    fi
fi

source ${VENV}/bin/activate

# Install dependencies
if command -v uv >/dev/null 2>&1; then
    echo "Using uv"
    uv pip install -r requirements.txt
else
    echo "uv not installed. Using pip"
    pip install -r requirements.txt
fi

if [ ! -f .env ]; then
    cp .env.example .env
    echo "Please go to NGC and generate an API key/URL pair and paste it in backend/.env"
fi