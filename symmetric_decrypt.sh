#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./symmetric_decrypt.sh <file_path>"
    exit 1
fi

python3 symmetric_decrypt.py "$1"