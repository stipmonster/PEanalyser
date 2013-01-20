#!/usr/bin/python

import os
import sys
import subprocess



bannedfunctions=open("./bannedfunctions.txt").readlines()
bannedfunctions =map(lambda x: x.replace("\n",""),bannedfunctions)  
rootdir = sys.argv[1]
#print bannedfunctions


for root, subFolders, files in os.walk(rootdir):
    for filename in files:
        if  "exe" in filename or "dll" in filename:
            filePath = os.path.join(root, filename)
            process = subprocess.Popen(["/usr/bin/readpe","-f","csv","-i",filePath], stdout=subprocess.PIPE)
            
            #exit_code = os.waitpid(process.pid, 0)
            output=process.communicate()[0]
            data=output.split("\n")
            for line in data:
                temp=line.split(',')
                if len(temp) >1:
                    #print temp
                    if temp[1] in bannedfunctions:
                        print temp[1]
