#!/usr/bin/python3
#CW3E Field Team
#Adolfo Lopez Miranda
#Solinst Levelogger

import serial
import datetime
from parse_fcn import Bytes2Hex, Hex2Binary, b2b, BCD2Dec
from command import solinst
import time

#Initilize serial connection
print("Initializing serial connection to Solinst levelogger!")
ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=None,
        xonxoff=False,
        rtscts=False,
        write_timeout=None,
        dsrdtr=False,
        inter_byte_timeout=None,
        exclusive=None)

ser.flushInput()
if ser.isOpen():
    try:
        while True:
            print("Connection to Solinst Levelogger Successful")
            input_command = input("Enter a command A-Z: ").upper()
            if len(input_command) == 1:
                ser.write(solinst(command))
                time.sleep(0.5)
                if ser.in_waiting > 0:
                    #read serial bytes
                    block = ser.read(ser.in_waiting)
                    print(block)
                    break
                else:
                    print('Enter a single character to continue.')
                    continue
    except serial.SerialException as e1:
        now = datetime.datetime.now()
        print("Error communicating with serial port: " + str(e1))
