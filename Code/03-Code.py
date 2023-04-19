#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, Justin H, and Nick A
# Uptime Sensor pt 2
# https://docs.python.org/3/library/email.examples.html

import os
import datetime
import time
import smtplib
from getpass import getpass

# Main
# ask the user for email and password
email = input("Please type your email: ")
password = getpass("Please type your email password: ")
up = "Server is up"
down = "Server is down"
target = input("IP address: ")

# Ping
def ping_Status(target):
    # Evaluate the response and assign success or failure to the status variable
    response = os.system("ping -c 1 " + target)
    if response == 0:
        status = up 
    else:
        status = down
    return status

# send an email if status changes
def send_email(status):
    # Create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # TLS 
    s.starttls()
    # Login
    s.login(email, password)
    # messages
    message = f"Your server is {status.lower()}"
    s.sendmail(email, email, message)
    # Close the SMTP session
    s.quit()

# Initial ping status
last_status = ping_Status(target)

while True:
    # Transmit a single ICMP ping packet to the target
    current_status = ping_Status(target)
    # If status has changed, send an email
    if current_status != last_status:
        send_email(current_status)
        last_status = current_status
    # Wait for 2 seconds before transmitting another ping packet
    time.sleep(2) 
# end