import pymongo
import sys
import re
import csv
from urlparse import urlparse

data=[]
def lookupcpe(cpeid = None):
    e = db.cpe.find_one({'id': cpeid})
    if e is None:
        return cpeid
    if 'id' in e:
        return e['title']


def info(): 
        return {"pluginName": "cveSearch", "version": (0,1),"Dep":
        [
        {"pluginName": "fileVersion","Version": (0,1)}
        ]
        }
def dep(array):
    data=array
    
def start(filename,pe):
#	connect = pymongo.Connection()
#	db = connect.cvedb
#	#collection = db.cves
#	collection = db.cpe
#	csvOutput=0
#	vSearch = data['ProductName']
#	if vSearch:
#	    for item in collection.find({"title": {'$regex' : vSearch + "$"}}):
#	        # the scvOutput module is far from finished !!
#			print "================================================="
#			print "CVE URI"
#			print item['id']