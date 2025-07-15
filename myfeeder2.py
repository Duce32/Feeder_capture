import tinytuya
import json
import time
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Display list of devices
#devices = c.getdevices()
#print("Device List: %r" % devices)

# Select a Device ID to Test
#id = "eba52a7430f310de12kqay"

# Display Properties of Device
#result = c.getproperties(id)
#print("Properties of device:\n", result)

# Display Status of Device
#result = c.getstatus(id)
#print("Status of device:\n", result)


#-------------------------------------------------------------------
def feed_pickles(num):

  c = tinytuya.Cloud(
        apiRegion=os.getenv("TINYTUYA_API_REGION"), 
        apiKey=os.getenv("TINYTUYA_API_KEY"), 
        apiSecret=os.getenv("TINYTUYA_API_SECRET"), 
        apiDeviceID=os.getenv("PICKLES_DEVICE_ID"))

  id=os.getenv("PICKLES_DEVICE_ID")

  commands = {
    "commands": [
        {"code": "manual_feed", "value": num }
    ]
}

  print("Sending command...")
  result = c.sendcommand(id,commands)
  print("Results\n:", result)

#-------------------------------------------------------------------
def feed_trixie(num):

  c = tinytuya.Cloud(
        apiRegion=os.getenv("TINYTUYA_API_REGION"), 
        apiKey=os.getenv("TINYTUYA_API_KEY"), 
        apiSecret=os.getenv("TINYTUYA_API_SECRET"), 
        apiDeviceID=os.getenv("TRIXIE_DEVICE_ID"))

  id=os.getenv("TRIXIE_DEVICE_ID")      

  commands = {
    "commands": [
        {"code": "manual_feed", "value": num }
    ]
}
  print("Sending command...")
  result = c.sendcommand(id,commands)
  print("Results\n:", result)

#-------------------------------------------------------------------


def main(args):
   if len(args) > 1:
    try:
          num = int(args[2])
    except ValueError:
         print("Invalid Value for portion ammount to send to the feeder")

    if args[1] == "trixie" :
         print("Feeding Trixie")
         feed_trixie(num)
    if args[1] == "pickles":
         print("Feeding Pickles")
         feed_pickles(num)
      

if __name__ == "__main__":
    main(sys.argv)