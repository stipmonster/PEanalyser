#!/usr/bin/python

import os
import sys
import subprocess
import pefile


def stackcookies(pe):
    mv2010=[0x55, 0x8b, 0xec, 0x83,0x33, 0xc5, 0x33, 0xcd,0xe8, 0xc3]
    count =0
    found =0
    pe.__data__.seek(0)
    for data in pe.__data__:
        for i in range(0, 10):
            if ord(data[0]) == mv2010[i] and found == i:
                found+=1
            if  found == 10:
                return 1
    return 0
def printinfo(check):
    if check:
        print "yes,",
    else:
        print "no,",
    
def start(filename,pe):
    print "# stack protection:"
    print
    
    print "ASLR,\"High entropy ASLR\",DEP/NX,SEH,\"Stack cookies (EXPERIMENTAL)\""
    
    
    
    DllCharacteristics = pe.OPTIONAL_HEADER.DllCharacteristics
    printinfo(DllCharacteristics & 0x40) #aslr
    printinfo(DllCharacteristics & 0x20) #hi aslr
    printinfo(DllCharacteristics & 0x100) #NX
    printinfo(not (DllCharacteristics & 0x400))#SEH
    printinfo(stackcookies(pe))
    print