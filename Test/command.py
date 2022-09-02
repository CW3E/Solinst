#!/usr/bin/python3
#CW3E Field Team
#Adolfo Lopez Miranda
#Solinst Levelogger Command's

#command's for Solinst levelogger
A = b'\x00\x61\xFF\x18\x24\x10' #read probe measurements
B = b'\x00\x62\xFF\x0A\x29\x60' #continue transferring test from A, K, and V commands
C = b'\x00\x63\xFF\x01\x00\x00\x00\x7B\x1C' #reads memory bank
D = b'\x00\x64\xFF\x00\x04\x1F\xFF\x00\xCF\x40'
E = b'\x00\x65\xFF\x10\x6B' #read date and time
F = b'\x00\x66\x08' + b'\x04\x73'#set date and time
G = b'\x00\67\xFF\x70\x6A' #command to read A/D values in 24 bits
H = b'\x00\x68\x01' #Enter bootstrap mood and save logging parameters - change last byte to 0x00 if not
I = b'\x00\x69\xFF'
J = b'\x00\x6A\xFF\xE0\x6E'
K = b'\x00\x6B\xFF\x35\x3B\xF0' #read current battery level, batter voltage, internal CPU temperature, software version, bootloader version, and one or more character extension indicating what firmware is installed
L = b''
M = b''
N = b'\x00\x6E\xFF\x20\x6C'
O = b''
P = b''
Q = b''
R = b''
S = b''
T = b'\x00\x74\xFF\x40\x67' #read the system address
U = b''
V = b''
W = W = b'\x00\x61\xFF\x2F\xF2\x51' #Wake-up - depth and tempeture
X = b''
Y = b''
Z = b'\x00\x7A\xFF\x04\x03\xFF\x00\x00\x7C\x0E' #initiates self-test

def solinst(command):
    if command == 'A':
        return A
    elif command == 'B':
        return B
    elif command == 'C':
        return C
    elif command == 'D':
        return D
    elif command == 'E':
        return E
    elif command == 'F':
        return F
    elif command == 'G':
        return G
    elif command == 'H':
        return H
    elif command == 'I':
        return I
    elif command == 'J':
        return J
    elif command == 'K':
        return K
    elif command == 'L':
        return L
    elif command == 'M':
        return M
    elif command == 'N':
        return N
    elif command == 'O':
        return O
    elif command == 'P':
        return P
    elif command == 'Q':
        return Q
    elif command == 'R':
        return R
    elif command == 'S':
        return S
    elif command == 'T':
        return T
    elif command == 'U':
        return U
    elif command == 'V':
        return V
    elif command == 'W':
        return W
    elif command == 'X':
        return X
    elif command == 'Y':
        return Y
    elif command == 'Z':
        return Z
