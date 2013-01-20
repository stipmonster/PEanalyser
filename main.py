#!/usr/bin/python

#import sys
#import os
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
import os
import sys
import subprocess
from multiprocessing import Process, Manager


def printinfo(check):
    for info in check:
        if info[0] != '':
            print info[1] + "\t",
    print
    
    
    
rootdir = sys.argv[1]
print "filename\tASLR\tHigh entropy ASLR\tDEP/NX\tSEH\tStack cookies (EXPERIMENTAL)\t"
for root, subFolders, files in os.walk(rootdir):
    for filename in files:
        if  "exe" in filename or "dll" in filename:
            filePath = os.path.join(root, filename)
            process = subprocess.Popen(["/usr/bin/pesec","-f","csv",filePath], stdout=subprocess.PIPE)
            
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
                print filename + "\t",
                printinfo(final)
            