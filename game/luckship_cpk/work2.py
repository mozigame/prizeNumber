# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

import requests
import re
import codecs 
from lxml import etree
import sys
import datetime
import time
import configparser
sys.path.append("../..")
import json
from   utils import configureRead
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
siteUrl='http://www.gdhpv.com/draw-center-service/resources/external/drawRecords/CQSSC?page=0&size=10'

def handler():
    bot_id = "468459314:AAGxpDlc1wXh-JzZA-4sGnxLSbIiawspBps"
    #https://api.telegram.org/bot468459314:AAGxpDlc1wXh-JzZA-4sGnxLSbIiawspBps/getUpdates
    #res=requests.get(url=configureRead.getJobValue(job_name,'site_url'),headers=headers,timeout=300)
    #online -250022899
    #test  -257257896
    #me 280720378
    data=urllib.parse.urlencode({ "chat_id": -250022899, "text": 'online test' }).encode('utf-8')
    #data=urllib.parse.urlencode({ "chat_id": '@channelsundy', "text": 'haha' }).encode('utf-8')
    result = urllib.request.urlopen("https://api.telegram.org/bot" + bot_id + "/sendMessage", data=data).read()
    print(result)

handler()
