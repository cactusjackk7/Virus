#!/usr/bin/python

import json, urllib, urllib2, argparse, hashlib, re, sys
from pprint import pprint

class vtAPI():
     def __init__(self):
         self.api = '<----------PRIVATE-API-KEY-GOES-HERE----->'
         self.base = 'https://www.virustotal.com/vtapi/v2/'

     def getReport(self,md5):
          param = {'resource':md5,'apikey':self.api,'allinfo': '1'}
          url = self.base + "file/report"
          data = urllib.urlencode(param)
          result = urllib2.urlopen(url,data)
          jdata = json.loads(result.read())
          return jdata

      def downloadFile(self,md5,name):
         try:
            param = {'hash':md5,'apiket':self.api}
            url = self.base + "file/download"
            data = urllib.urlencode(param)
            req = urllib2.Request(url,data)
            result = urllib2.urlopen(req)
            downloadfile = result.read()
            if len(downloadfile) > 0:
               fo = open(name, 'wb')
               fo.write(downloadfile)
               fo.close()
               print "\n\tMalware Downloaded to File -- " + name
            else:
               print md5 + " -- Not Found for Download"
            except Exception:
               print md5 + " -- Not Found for Download"
      def
