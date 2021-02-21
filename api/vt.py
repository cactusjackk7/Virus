#!/usr/bin/python

import json, urllib, urllib2, argparse, hashlib, re, sys
from pprint import pprint

class vtAPI():
     def __init__(self):
         self.api = '<----------PRIVATE-API-KEY-GOES-HERE----->'
         self.base = 'https://www.virustotal.com/vtapi/v2/'

     def getReport(self,md5):
          param = {'resource':md5,'apikey':self.api,'allinfo': '1'}
          url = self
