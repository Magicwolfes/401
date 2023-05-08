#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, and Nick A


# Import
import time

# Function 1

def mode1():
    # User inpit word list file path
    filepath = input("Enter your dictionary filepath:\n")
    #Open the file 
    file = open(filepath)
    line = file.readline()
    # Iterate through each word in given list
    while line:
        line = line.rstrip()
        word = line
        time.sleep(1)
        print(word)
        line = file.readline()
    file.close()

def mode2():
    filepath = input("Enter your dictionary filepath:\n")
    password = input("Please type your new password: \n")
    with open(filepath) as file:
        while True:
            for line in file:
                if line.strip() == password:
                    print("Password is weak! Try again")
                    return
                else:
                     print("Password is strong!")
                     break

   
while True:
    answer = input("Mode 1 or Mode 2: ")
    if answer == "Mode 1":
        mode1()
    if answer == "Mode 2":
        mode2()
    else:
        break
# end