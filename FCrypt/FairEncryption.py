from FCrypt.BasicEncryption import BasicEncryption

BE = BasicEncryption()

def encrypt_text(unencrypted_data:str):
    return BE.encrypt_string(unencrypted_data)

def decrypt_text(encrypted_data):
    return BE.decrypt_string(encrypted_data)

def encrypt_file(file_name_and_path:str):
    return BE.encrypt_file(file_name_and_path)

def decrypt_file(file_name_and_path:str):
    return BE.decrypt_file(file_name_and_path)

if __name__ == '__main__':
    clear = "what up!"
    c = encrypt_text(clear)
    print(c)
