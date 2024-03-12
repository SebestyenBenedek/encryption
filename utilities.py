def read_file_content(file_path, access_type):
    try:
        with open(file_path, access_type) as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def shift_content(content, shift_by):
    shifted_content = ''
    for i in range(len(content)):
        char = content[i]
        shifted_content += chr((ord(char) + shift_by))
    return shifted_content
    
def reverse_content(content):
    return content[::-1]

def xor_content_with_key(content, key):
    xored_content = bytearray()

    for i in range(len(content)):
        xored_content.append(content[i % len(content)] ^ key[i % len(key)])
    return xored_content