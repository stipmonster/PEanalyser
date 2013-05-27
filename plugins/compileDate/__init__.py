import os
import pefile
import datetime

def info(): 
        return {"pluginName": "compileDate", "Version": (0,1)}

def start(filename,pe,addToarray):
    print "## compile date:"
    print
    print(datetime.datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp).strftime('%d-%m-%Y %H:%M:%S'))
