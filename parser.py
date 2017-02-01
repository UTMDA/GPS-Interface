'''
Title: GPS - Parser
Purpose: To recieve and send useful GPS data
Important Note: 'pynmea' & 'pyserial' libraries are needed. Compatible with python3

Author: Amal G Jose
Edit By: Edward Y. Liu
Last Modified Date: January 31, 2017
'''

# GPS signal test

'''

import serial

port = 'name'

ser = serial.Serial()
ser.baudrate = 9600
ser.port = port
ser.open()

while True:
    print(ser.readline())

'''


# GPS signal parser

import time
import serial
import string
from pynmea import nmea

# define port, baudrate, & frequency
port_ = 'name';
baudrate_ = 9600
timeout_ = 1

# initialize serial
ser = serial.Serial()
ser.port = port_    # if invalid port, then SerialException Error - could not open port 'name' is inevitable
ser.baudrate = baudrate_
ser.timeout = timeout_
ser.open()
gpgga = nmea.GPGGA()

while True:
    data = ser.readline()
    if data[0:6] == '$GPGGA':
        ##method for parsing the sentence
        gpgga.parse(data)
        lats = gpgga.latitude
        print("Latitude values : " + str(lats))

        lat_dir = gpgga.lat_direction
        print("Latitude direction : " + str(lat_dir))

        longitude = gpgga.longitude
        print("Longitude values : " + str(longitude))

        long_dir = gpgga.lon_direction
        print("Longitude direction : " + str(long_dir))

        time_stamp = gpgga.timestamp
        print("GPS time stamp : " + str(time_stamp))

        alt = gpgga.antenna_altitude
        print("Antenna altitude : " + str(alt))

        lat_deg = lats[0:2]
        lat_mins = lats[2:4]
        lat_secs = round(float(lats[5:])*60/10000, 2)

        latitude_string = lat_deg + u'\N{DEGREE SIGN}' + lat_mins + string.printable[68] + str(lat_secs) + string.printable[63]
        print("Latitude : " + str(latitude_string))

        lon_deg = longitude[0:3]
        lon_mins = longitude[3:5]
        lon_secs = round(float(longitude[6:])*60/10000, 2)
        lon_str = lon_deg + u'\N{DEGREE SIGN}' + lon_mins + string.printable[68] + str(lon_secs) + string.printable[63]
        print("Longitude : " + str(lon_str))