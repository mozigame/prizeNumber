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

import logging
import logging.config
import codecs
import yaml
from notice.groupNotice import *
logging.config.dictConfig(yaml.load(codecs.open("conf/logger.yml", 'r', 'utf-8').read()))

logger = logging.getLogger("noticeparser")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36'}


class prizeNotice():
   
    

    def __init__(self,url):
        self.url=configureRead.getCommonValue('concurrent',url)
        
        

    def notice_to_draw_server(self,items):
        for item in items:
            self._notice_to_draw_server(item)
            
    def _notice_to_draw_server(self,item):
        current_item=spiderRecord4DB.get_recent_item(item.code,item.issue)
        is_same=True
        numbers=''
        priority=0
        for it in current_item:
            priority=priority+it[7]
            if(len(numbers)<1):
                numbers=it[3]
                continue
            if(numbers!=it[3]):
                is_same=False
        
        
        server_url=self.url+"?code="+item.code+"&&issueAlias="+item.issue+"&&priority="+str(priority)
            
        if(is_same==False):
            server_url=server_url+"&&status="+str(4)
        logger.info('server url :'+server_url)
        try:
            res=requests.post(url=server_url,headers=headers,timeout=300)
            logger.info("response :"+res.text)
        except Exception as e:
            logger.warn('notice '+'   error for :'+" error:"+str(e))
            _group_notice = groupNotice()
            _group_notice.notice_to_group('notice '+'   error for :'+" error:"+str(e))
        
        
        
