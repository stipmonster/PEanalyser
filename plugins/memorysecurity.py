#!/usr/bin/python

import os
import sys
import subprocess

def printinfo(check):
    for info in check:
        if info[0] != '':
            print info[1] + ",",
    print

def start(filename):
    print "# stack protection:"
    print
    
    print "ASLR,\"High entropy ASLR\",DEP/NX,SEH,\"Stack cookies (EXPERIMENTAL)\""
    process = subprocess.Popen(["/usr/bin/pesec","-f","csv",filename], stdout=subprocess.PIPE)
            
            #exit_code = os.waitpid(process.pid, 0)
    output=process.communicate()[0]
    data=output.split("\n")
    if "ASLR" in output:
        final =[]
        for line in data:
            if line =="Certificates":
                break
            temp=line.split(',')
            final.append(temp)
        printinfo(final)
            