#!/usr/bin/python

import os
import sys
import subprocess
import plugin
def info(): 
        return {"pluginName": "bannedFuncion", "Version": (0,1)}
        
def run(filename,pe):
    print "## banned function:"
    path= os.path.dirname(os.path.abspath(__file__))
    path = path + "/bannedfunctions.txt"
    bannedfunctions=open(path).readlines()
    bannedfunctions =map(lambda x: x.replace("\n",""),bannedfunctions)  
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
      for imp in entry.imports:
        if imp.name in bannedfunctions:
            print imp.name