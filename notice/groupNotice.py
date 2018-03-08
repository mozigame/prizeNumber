# coding:utf-8
'''
Created on 2017-10-13

@author: shawn
'''


import requests
import re
from lxml import etree
from utils import configureRead
from store import spiderRecord4DB
from utils import configureRead
import logging
import logging.config
import codecs
import yaml
import urllib.request
logging.config.dictConfig(yaml.load(codecs.open("conf/logger.yml", 'r', 'utf-8').read()))

logger = logging.getLogger("groupparser")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36'}


class groupNotice():
   
    

    def __init__(self):
        self.bot_id = "468459314:AAGxpDlc1wXh-JzZA-4sGnxLSbIiawspBps"
        self.chat_id=int(configureRead.getCommonValue('concurrent', 'group'))
        

    def notice_to_group(self,content):
        
        try:
            data=urllib.parse.urlencode({ "chat_id": self.chat_id, "text": content}).encode('utf-8')
            result = urllib.request.urlopen("https://api.telegram.org/bot" + self.bot_id + "/sendMessage", data=data,timeout=300).read()
            
            logger.info("response :"+str(result))
        except Exception as e:
            logger.warn('notice '+'   error for :'+" error:"+str(e))
            
    
        
        
        
