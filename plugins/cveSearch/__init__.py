import pymongo
import sys
import re
import csv
from urlparse import urlparse



def lookupcpe(cpeid = None):
    e = db.cpe.find_one({'id': cpeid})
    if e is None:
        return cpeid
    if 'id' in e:
        return e['title']

def findranking(cpe = None, loosy = True):
    if cpe is None:
        return False
    r = db.ranking
    result = False
    if loosy:
        for x in cpe.split(':'):
            if x is not '':
                i = r.find_one({'cpe': {'$regex':x}})
            if i is None:
                continue
            if 'rank' in i:
                result = i['rank']
    else:
        i = r.find_one({'cpe': {'$regex':cpe}})
        print (cpe)
        if i is None:
            return result
        if 'rank' in i:
            result = i['rank']

    return result

def info(): 
        return {"pluginName": "bannedFuncion", "Version": (0,1),Dep:
        [
        {"pluginName": "fileVersion","Version": (0,1)}
        ]
        }

def start(filename,pe):
	connect = pymongo.Connection()
	db = connect.cvedb
	#collection = db.cves
	collection = db.cpe
	csvOutput=0
	vSearch = data['ProductName']
	if vSearch:
	    for item in collection.find({"title": {'$regex' : vSearch + "$"}}):
	        # the scvOutput module is far from finished !!
			print "================================================="
			print "CVE URI"
			print item['id']