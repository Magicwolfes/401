#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, Justin H, and Nick A
# File Encrytption Script

from cryptography.fernet import Fernet

# Prompt User
Choices = {
    "Mode 1": "Encrypt F",
    "Mode 2": "Decrypt F",
    "Mode 3": "Encrypt M",
    "Mode 4": "Decrypt M"   
}
method_choice = input("Pick one of the following choices: \n Mode 1) Encrypt file\n Mode 2) Decrypt File\n Mode 3) Encrypt Message\n Mode 4) Decrypt Message\n")
method = Choices.get(method_choice)

# Functions to write key and load key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# Write key and load key
write_key()
key = load_key()

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        original_data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(original_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

if method == "Encrypt F":
    file_path = input("Please type the file path you'd like to encrypt: ")
    encrypt_file(file_path, key)

if method == "Decrypt F":
    file_path = input("Please type the file path you'd like to decrypt: ")
    decrypt_file(file_path, key)

if method == "Encrypt M":
    message = input("Please type the message you'd like to encrypt: ")
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted message: {encrypted_message}")

if method == "Decrypt M":
    encrypted_message = input("Please type the message you'd like to decrypt: ")
    decrypted_message = decrypt_message(encrypted_message.encode(), key)
    print(f"Decrypted message: {decrypted_message}")
