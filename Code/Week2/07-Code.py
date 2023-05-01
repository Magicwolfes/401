#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, Justin H, and Nick A
# File Encrytption Script
# Chatgpt -> helped with the formating 
import os
from cryptography.fernet import Fernet

# Functions to write key and load key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# Write key 
write_key()

 # Function to encrypt a file
def enc_file(file_path, key):
    with open(file_path, "rb") as file:
        original_data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(original_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
        
        
  # Function to decrypt a file   
def dec_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
        
            
while True:
 # Get user input
    choice = input("Encrypt or Decrypt or Exit? ")  
    if choice not in ["Encrypt", "Decrypt", "Exit"]:
        print("Invalid choice. Please try again.")
        continue
    
    start_directory = input("Please write the directory path: ") 
    key = load_key()
    # Recursively encrypt a single folder and all its contents.
    if choice == "Encrypt":
        # Walk through all directories and files in the starting directory
        for root, dirs, files in os.walk(start_directory):
            for file_name in files:
                # Construct the file path relative to the starting directory
                file_path = os.path.join(root, file_name)
                print("Encrypting file: " + file_path)
                enc_file(file_path, key)
    # Exit            
    if choice == "Exit":
        break
        
    # Recursively decrypt a single folder that was encrypted by this tool
    elif choice == "Decrypt":  
        # Walk through all directories and files in the starting directory
        for root, dirs, files in os.walk(start_directory):
            for file_name in files:
                # Construct the file path relative to the starting directory
                file_path = os.path.join(root, file_name)
                print("Decrypting file: " + file_path)
                dec_file(file_path, key)
    
