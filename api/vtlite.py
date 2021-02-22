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
		# Md5 Function
		
		def checkMD5(checkval):
			if re.match(r"([a-fA-F\d]{32})", checkval) == None:
				md5 = md5sum(checkval)
				return md5.upper()
			else: 
				return checkval.upper()
			
		def md5sum(filename):
			fh = open(filename, 'rb')
			m = hashlib.md5()
			while True:
					data = fh.read(8192)
					if not data:
							break
					m.update(data)
			return m.hexdigest() 
		
		def parse(it, md5, verbose, jsondump):
			if it['response_code'] == 0:
				print md5 + " -- Not Found in VT"
				return 0
			print "\n\tResults for MD5: ",it['md5'],"\n\n\tDetected by: ",it['positives'],'/',it['total'],'\n'
			if 'Sophos' in it['scans']:
				print '\tSophos Detection:',it['scans']['Sophos']['result'],'\n'
			if 'Kaspersky' in it['scans']:
				print '\tKaspersky Detection:',it['scans']['Kaspersky']['result'], '\n'
			if 'ESET-NOD32' in it['scans']:
				print '\tESET Detection:',it['scans']['ESET-NOD32']['result'],'\n'
				
			print '\tScanned on:',it['scan_date']
			
			if jsondump == True:
				jsondumpfile = open("VTDL" + md5 + ".json", "w")