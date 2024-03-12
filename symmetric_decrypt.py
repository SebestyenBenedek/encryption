import sys
import os
import json
import base64
from utilities import *
from getpass import getpass
from json_decoder import custom_decoder

shift_by = -3

def xor_binary_content(binary_content, key):
    binary_key = key.encode('utf-8')
    return xor_content_with_key(binary_content, binary_key).decode('utf-8')

def decrypt(content, key):
    return shift_content(reverse_content(xor_binary_content(content, key)), shift_by)

def get_account_by_domain(file_path: str, key: str, domain_name: str):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                current_data = json.load(f, object_hook=custom_decoder)
                if domain_name in current_data:
                    account = current_data[domain_name]
                    decrypted_username = decrypt(base64.b64decode(account['username']), key)
                    decrypted_password = decrypt(base64.b64decode(account['password']), key)
                    print(
                        f"{domain_name} account: \nusername: {decrypted_username}\npassword: {decrypted_password}"
                    )
                else:
                    print("Error: The domain name is incorrect, or there isn't any account at this domain name.")
            except json.JSONDecodeError:
                print("Error: Invalid JSON format in the file.")
    else:
        print("Error: The file path is incorrect, or the file doesn't exist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 symmetric_decrypt.py <file_path> <domain_name>")
        key = getpass("Enter your key:")
        file_path = input("Enter the path to the file: ")
        domain_name = input("Domain name: ")
    else:
        key = getpass("Enter your key:")
        file_path = sys.argv[1]
        domain_name = sys.argv[2]

    get_account_by_domain(file_path, key, domain_name)