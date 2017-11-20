#!/usr/bin/env python


'''

Simple script that reads serial data from the Arduino attached to whatever port.


'''


# adjust this to taste
port = "/dev/ttyUSB0"





import time, os, serial 


print "Connecting to %s..." % port
ser = serial.Serial(port, 9600, timeout=.5)

print "Success!"



def read_buffer():

    # read the whole buffer
    last_data=''
    while True:
        data=ser.readline()
        if data:
            last_data=data
        else:
            return last_data.replace("\n", "")





while True:

    in_data=ser.readline()

    if in_data:
       in_data=in_data.replace("\n", "") 
       in_data=in_data.replace("\r", "") 
       
       part = in_data.split(",")
       print in_data
       print part
       
       data={}
       
       for p in part:
         parts = p.split(":")
         print parts
         
         if parts[0] == "Wind Speed":
           data['windSpeed'] = float(parts[1])
         elif parts[0] == "Wind Compass":
           data['windDir'] = float(parts[1])

            # these might have to be renamed
            #data['temperature'] = float(parts[2])
            #data['barometer'] = float(parts[3])

         print data
    

