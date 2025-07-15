#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os

# set #6 as SW520D Pin

Sw520dPin=18 
PIR_PIN = 4

#print message at the begining ---custom function
def print_message():

    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    

def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Sw520dPin,GPIO.IN)
    GPIO.setup(PIR_PIN, GPIO.IN)

def check_pir():
# This is the check motion of whats in the trixie crate.  Hopefully it will be trixie
    x=0
    print("PIR Module detection for trixie")
    print("Ready")
    while x==0:
          if GPIO.input(PIR_PIN):
                print("Trixie Detected!")
                # If we detected motion meaning trixie hopefully, then we will drop her food, and then drop pickles food
                os.system('python /home/metalo/src/120.py')
                os.system('/home/metalo/src/.venv/bin/python /home/metalo/src/myfeeder2.py trixie 3')
                time.sleep(15)
                os.system('/home/metalo/src/.venv/bin/python /home/metalo/src/myfeeder2.py pickles 3')
                x=1  #Motion found so feed them only one time
    time.sleep(300)
    os.system("python /home/metalo/src/open.py")
#main function
def main():
    x = 0
    print_message()
    while x == 0:
        #read Sw520dPin's level
        if (GPIO.input(Sw520dPin)) or (GPIO.input(PIR_PIN)):
            # Check for the door tilt, and if it did tilt, then lock the door behind trixie
            os.system('python /home/metalo/src/120.py')
            x = 1   # Exit out of the while loop
        else:

            print ('================================')
            print ('=    Trixie door  Not tilt...  =')
            print ('================================')
            print ('\n')
            time.sleep(1)

#   Second phase is to check if the PIR sensor detects trixie is in the crate, sometimes she will
#   Weasel her way back out so we go into the Check Motion Phase inside the crate
    check_pir()

#define a destroy function for clean up everything after the script finished
def destroy():

    GPIO.cleanup()

if __name__ == '__main__':

    setup()
    main()
    destroy()

        
        





    
