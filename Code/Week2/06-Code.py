#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, Justin H, and Nick A
# File Encrytption Script
# Used Chatgpt > to help with the functions

from cryptography.fernet import Fernet

# Functions to write key and load key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# Write key and load key
write_key()

while True:
    
    # Prompt User
    Choices = {
        "Mode 1": "Encrypt F",
        "Mode 2": "Decrypt F",
        "Mode 3": "Encrypt M",
        "Mode 4": "Decrypt M", 
        "Mode 5": "Exit" 
    }
    method_choice = input("Pick one of the following choices: \n Mode 1) Encrypt file\n Mode 2) Decrypt File\n Mode 3) Encrypt Message\n Mode 4) Decrypt Message\n Mode 5) Exit\n")
    method = Choices.get(method_choice)

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
        plaintext = message.encode('utf-8')
        f = Fernet(key)
        encrypted = f.encrypt(plaintext)
        print("The encrypted message is: " + encrypted.decode('utf-8'))

    # Function to decrypt a message
    def decrypt_message(encrypted_message, key):
        ciphertext = encrypted_message.encode('utf-8')
        f = Fernet(key)
        decrypted = f.decrypt(ciphertext)
        print("The decrypted message is: " + decrypted.decode('utf-8'))

    if method == "Encrypt F":
        file_path = input("Please type the file path you'd like to encrypt: ")
        encrypt_file(file_path, key)
        print("Your file has been encrypted")

    if method == "Decrypt F":
        file_path = input("Please type the file path you'd like to decrypt: ")
        decrypt_file(file_path, key)
        print("Your file has been decrypted")
    if method == "Encrypt M":
        message = input("Please type the message you'd like to encrypt: ")
        encrypt_message(message, key)

    if method == "Decrypt M":
        encrypted_message = input("Please type the message you'd like to decrypt: ")
        decrypt_message(encrypted_message, key)
    if method == "Exit":
        break