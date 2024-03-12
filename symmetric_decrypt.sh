#!/bin/bash

if [ -z "$2" ]; then
    echo "Usage: ./symmetric_decrypt.sh <file_path> <domain_name>"
    exit 1
fi

python3 symmetric_decrypt.py "$1" "$2"