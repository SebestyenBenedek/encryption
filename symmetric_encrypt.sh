#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./symmetric_encrypt.sh <file_path>"
    exit 1
fi

python3 symmetric_encrypt.py "$1"