from __future__ import print_function
from sqlite3 import Time
from tkinter.tix import Tree
from dronekit import Rangefinder, connect, VehicleMode
import time
#Set up option parsing to get connection string
import argparse  
import pyrebase

firebaseConfig={"apiKey": "AIzaSyDubuVKj7XYrnp3yX3x5YPFfX-m8z0GEPU",
  "authDomain": "pyrebaserealtime-example.firebaseapp.com",
  "databaseURL": "https://pyrebaserealtime-example-default-rtdb.firebaseio.com",
  "projectId": "pyrebaserealtime-example",
  "storageBucket": "pyrebaserealtime-example.appspot.com",
  "messagingSenderId": "101749055169",
  "appId": "1:101749055169:web:69909934e038b47fa63e40",
  "measurementId": "G-TXX3Y2YDRJ"}


parser = argparse.ArgumentParser(description='Print out vehicle state information. Connects to SITL on local PC by default.')
parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()
connection_string = '/dev/ttyACM0'
sitl = None
print("\nConnecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

vehicle.wait_ready('autopilot_version')

print(" Autopilot Firmware version: %s" % vehicle.version)
print(" Groundspeed: %s" % vehicle.groundspeed)
print(" Airspeed: %s" % vehicle.airspeed)    # settable
print(" Global Location: %s" % vehicle.location.global_frame)
# print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
print(" Altitude: %s" % vehicle.location.global_relative_frame.alt)
print(" Attitude: %s" % vehicle.attitude)
print(" GPS: %s" % vehicle.gps_0)

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

while True:
  coordinate={"Distance From Home":"50"+" m",
      "Longitude": vehicle.location.global_relative_frame.lon,
      "Latitude": vehicle.location.global_relative_frame.lat,
      "Altitude": vehicle.location.global_relative_frame.alt
      }
  db.child("vehicle_coordinate").set(coordinate)

  attitude={"Pitch": vehicle.attitude.pitch,
      "Yaw": vehicle.attitude.yaw,
      "Roll": vehicle.attitude.roll}
  db.child("vehicle_attitude").set(attitude)

  speed={"Ground Speed":vehicle.groundspeed,
      "Vertical Speed":vehicle.airspeed}
  db.child("vehicle_speed").set(speed)

  time.sleep(0.2)