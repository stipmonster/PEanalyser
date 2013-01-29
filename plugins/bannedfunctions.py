#!/usr/bin/python

import os
import sys
import subprocess


def start(filename):
    print "# banned function:"
    print
    bannedfunctions=open("./plugins/bannedfunctions.txt").readlines()
    bannedfunctions =map(lambda x: x.replace("\n",""),bannedfunctions)  
    process = subprocess.Popen(["/usr/bin/readpe","-f","csv","-i",filename], stdout=subprocess.PIPE)
            
        #exit_code = os.waitpid(process.pid, 0)
    output=process.communicate()[0]
    data=output.split("\n")
    for line in data:
        temp=line.split(',')
        if len(temp) >1:
            if temp[1] in bannedfunctions:
               print temp[1]
