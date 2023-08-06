import pickle
from Crypto.Cipher import AES
import os

def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print("Error:", e)

def load_pickle_data(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    
    decrypted_file_path = encrypted_file_path[:-4]  # Menghapus ekstensi .enc
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(data)
    
    print("File berhasil didekripsi:", decrypted_file_path)

# Contoh penggunaan
key_path = 'key.ssg'
kuncinya = load_pickle_data(key_path)

for root, dirs, files in os.walk("C:/Users/Lenovo/Desktop/python/Chess"):
    for file in files:
        file_path = os.path.join(root, file)
        # Mengganti '\' dengan '/'
        file_path = file_path.replace('\\', '/')
        
        encrypted_file_path = file_path
        key = kuncinya

        decrypt_file(encrypted_file_path, key)
        delete_file(encrypted_file_path)
delete_file(key_path)