#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, and Nick A
# Event Logging Tool Part 3 of 3

import logging
import os
import datetime
import logging.handlers as handlers
import time

target = "8.8.8.8"

# Create loggers
logger = logging.getLogger()

#print to screen logger
Slogger = logging.Streamhandler()

#print to file
Flogger = logging.Filehandler('Demo.log')

#Set levels
Shandler.setLevel(logging.ERROR)
Fhandler.setlevel(logging.DEBUG)

# Create formatter 
SFormat = logger.Format('%(name)s - %(levelname)s - %(message)s')
FFormat = logger.Format('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add format to handlers 
Fhandler.setFormat(FFormat)
Shandler.setFormat(SFormat)

# add handlers to loggers
Slogger.addHandler(Shandler)
Flogger.addHandler(Fhandler)
                   
def ping_Status(target):
    try:
        # Intentionally raise an exception to simulate an error
        raise ValueError("An intentional error occurred")
        # Evaluate the response and assign success or failure to the status variable
        icmp = os.system("ping -c gg1 " + target)
        if icmp == 0
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
      Flogger.exception("Debugging now ")
      Slogger.exception("An error has occurred ")
    
        raise e
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
        Flogger.exception("Debugging now ")
        Slogger.exception("An error has occurred ")

    
