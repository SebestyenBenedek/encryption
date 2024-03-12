import sys
import json
import base64
import os
from utilities import *
from getpass import getpass
from json_decoder import custom_decoder
from json_encoder import CustomEncoder

shift_by = 3

def xor_content(content, key):
    binary_content = content.encode('utf-8')
    binary_key = key.encode('utf-8')
    return xor_content_with_key(binary_content, binary_key)

def encrypt(content):
    return xor_content(reverse_content(shift_content(content, shift_by)), key)

def add_account_to_file(file_path: str, domain_name: str, username: bytearray, password: bytearray):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
            if content:
                current_data = json.loads(content.decode('utf-8'), object_hook=custom_decoder)
            else:
                current_data = {}
    else:
        current_data = {}

    current_data[domain_name] = {
        "username": base64.b64encode(username).decode('utf-8'),
        "password": base64.b64encode(password).decode('utf-8')
    }
    with open(file_path, 'w') as f:
        json.dump(current_data, f, ensure_ascii=False, cls=CustomEncoder)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 symmetric_encrypt.py <file_path> <domain_name> <username> <password>")
        key = getpass("Enter your key:")
        file_path = input("Enter the path to the file: ")
        domain_name = input("Domain name: ")
        username = encrypt(input("Username: "))
        password = encrypt(getpass("Password: "))
    else:
        key = getpass("Enter your key:")
        file_path = sys.argv[1]
        domain_name = sys.argv[2]
        username = encrypt(sys.argv[3])
        password = encrypt(sys.argv[4])

    add_account_to_file(file_path, domain_name, username, password)
        