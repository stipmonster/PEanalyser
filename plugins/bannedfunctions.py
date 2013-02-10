#!/usr/bin/python

import os
import sys
import subprocess


def start(filename,pe):
    print "# banned function:"
    print
    bannedfunctions=open("./plugins/bannedfunctions.txt").readlines()
    bannedfunctions =map(lambda x: x.replace("\n",""),bannedfunctions)  
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
      for imp in entry.imports:
        if imp.name in bannedfunctions:
            print imp.name