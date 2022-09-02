#!/usr/bin/python3
#CW3E Field Team
#Adolfo Lopez Miranda
#fucntions to be used for Numerical System conversions, and Bit Manipulation process

import numpy as np
import pandas as pd
import csv
import binascii 

#Bytes2Hex will convert serial bytes to their Hexadecimal Representation
def Bytes2Hex(serial_bytes):
    hex_str = binascii.hexlify(serial_bytes) #converts each serial byte to its hexadcimal representation
    n = 2
    hex_list = [hex_str[i:i+n] for i in range(0, len(hex_str),n)]
    return hex_list

#Hex2Binary will convert Hexadecimal Representation for each byte to their binary equivalent 
def Hex2Binary(hex_output):
    result = ''
    for a in hex_output:
        scale = 16
        result += bin(int(a,scale))+' ' #converts and returns binary equivalent string of a given integer
        bin_split = result.split("0b") #remove leading "0b"
        b_str = ' '.join(map(str,bin_split))
        binary = b_str.split()
    return binary

#b2b will convert each binary string to their decimal equivalent
def b2b(bin_arr):
    x = int(bin_arr,2)  
    return x

#BCD2Dec will convert Binary coded decimal representation to its decimal equivalent 
def BCD2Dec(bcd):
    parse = int((bcd >> 4)*10 + (bcd & 0xF))
    return parse
