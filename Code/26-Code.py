#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, and Nick A
# Event Logging Tool Part 1 of 3


import logging
import os
import datetime
import time

target = "8.8.8.0"

def ping_Status(target):
    try:
         #Intentionally raise an exception to simulate an error
        raise ValueError("An intentional error occurred")   
        # Evaluate the response and assign success or failure to the status variable
        icmp = os.system("ping -c 1 " + target)
        if icmp == 0:
            status = "success"
            print(f"{target} is up!")
        else:
            status = "failure"
            print(f"{target} is down!")
        
        # Get the current timestamp and print the status and timestamp
        currenttime = datetime.datetime.now()
        print(f"{currenttime} - Status: {status}")
        return status
    except Exception as e:
        logger.exception("An error occurred")
        raise e

# Create and configure logger
logging.basicConfig(filename="Demo.log", format='%(asctime)s %(message)s', filemode='w')

# Create object
logger = logging.getLogger()

# Setting the threshold
logger.setLevel(logging.DEBUG)

while True:
    try:
        # Transmit a single ICMP ping packet to the target
        ping_Status(target)
        # Wait for 2 seconds before transmitting another ping packet
        time.sleep(2)
    except KeyboardInterrupt:
        # Stop the program if the user interrupts it
        break
    except Exception as e:
        logger.exception("An error occurred")
