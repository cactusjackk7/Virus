#!/usr/bin/python
mport json, urllib, urllib2, argparse, hashlib, re, sys
from pprint import pprint

class vtAPI():
	def __init__(self):
		self.api = '<--------------PUBLIC-API-KEY-GOES-HERE----->'
		self.base = 'https://www.virustotal.com/vtapi/v2/'
		
	def getReport(self,md5):
		param = {'resource':md5,'apikey':self.api}
		url = self.base + "file/report"
		data = urllib.urlencode(param)
		result = urllib2.urlopen(url,data)
		jdata =  json.loads(result.read())
		return jdata
	
	def rescan(self,md5):
		param = {'resource':md5,'apikey':self.api}
		url = self.base + "file/rescan"
		data = urllib.urlencode(param)
		result = urllib2.urlopen(url,data)
		print "\n\tVirus Total Rescan Initiated for -- " + md5 + " (Requery in 10 Mins)"
		
