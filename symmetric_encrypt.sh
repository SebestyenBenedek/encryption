#!/bin/bash

if [ -z "$4" ]; then
    echo "Usage: ./symmetric_encrypt.sh <file_path> <domain_name> <username> <password>"
    exit 1
fi

python3 symmetric_encrypt.py "$1" "$2" "$3" "$4"