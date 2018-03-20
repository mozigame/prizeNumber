# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''
from threading import Thread
from time import sleep
from random import randint
import imp
import time

from store import spiderRecord4DB
from utils import configureRead
from notice.prizeNotice import *
from notice.groupNotice import *
import sys

import logging
import logging.config
import codecs
import yaml
logging.config.dictConfig(yaml.load(codecs.open("conf/logger.yml", 'r', 'utf-8').read()))

logger = logging.getLogger("threadparser")

class SpiderThread(Thread):
    """docstring for MyThread"""
    def __init__(self, name):
        super(SpiderThread, self).__init__()
        self.name = name       
    def run(self):
            
            
            '''
            while(True):
                print(self.name)
                time.sleep(3)
            '''
            while(True):
                
                try:
                    current_prize_number=spiderRecord4DB.getCurrentPrizeNumberFromDB(self.name)
                    logger.info('Thread '+self.name+'   get  item :'+" :44") 
                
                    fp, pathname, description = imp.find_module('work',['./game/'+self.name])
                    logger.info('Thread '+self.name+'   get  item :'+" :47") 
                    m = imp.load_module(self.name+"_work", fp, pathname, description)
                    logger.info('Thread '+self.name+'   get  item :'+" :49") 
                    items=m.handler(self.name,current_prize_number)
                    logger.info('Thread '+self.name+'   get  item :'+" :51") 
                    logger.info('Thread '+self.name+'   get  item :'+" :"+''.join(items))
                    if(items and len(items)>0):
                        spiderRecord4DB.batchInsert(items)
                        logger.info('Thread '+self.name+'   batchinsert :'+" :"+''.join(items))
                        logger.info('Thread '+self.name+'   get  item :'+" :55")
                        spiderRecord4DB.batchUpdate(items)
                        logger.info('Thread '+self.name+'   batchupdate :'+" :"+''.join(items))
                        logger.info('Thread '+self.name+'   get  item :'+" :57")
                        
                        notice = prizeNotice('prize_notice_server')
                        notice.notice_to_draw_server(items)
                        logger.info('Thread '+self.name+'   noticetoserver :'+" :"+''.join(items))
                        logger.info('Thread '+self.name+'   get  item :'+" :61") 
                        
                except Exception as e:
                    logger.warn('Thread '+self.name+'   error for :'+" error:"+str(e)) 
                    _group_notice = groupNotice()
                    _group_notice.notice_to_group('Thread '+self.name+'   error for :'+" error:"+str(e))
                finally:
                    if fp:
                        fp.close()
                time.sleep(int(configureRead.getJobValue(self.name, 'sleepTimeInThread')))
            


    
       