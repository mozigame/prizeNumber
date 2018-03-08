# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from SpiderThread import SpiderThread
from utils import configureRead
import time
import logging
import logging.config
import codecs
import yaml
logging.config.dictConfig(yaml.load(codecs.open("conf/logger.yml", 'r', 'utf-8').read()))

logger = logging.getLogger("mainparser")


def execute(model_name=''):

    thread = SpiderThread(model_name)
    threads.append(thread)
    thread.setDaemon(True)
    thread.start()


if __name__ == "__main__":
    threads = []

    while(True):
        is_alive=0
        #execute('guanxi11_5')
        logger.info("main thread working now "+str(threads))
        for job in  configureRead.get_section():
            if('opencai'==job):
                continue
            
            if('gdhpv'==job):
                continue
           
            #execute(job)
            
            if(len(threads)==0):
                execute(job)
                logger.info(" thread  "+job+" is working  now !")
            else:
                is_alive=0
                for th in threads:
                    if(th.name==job):
                        
                        if(th.is_alive()):
                            logger.info(" thread  "+th.name+" is alive,so i'll do nothing for it!")
                            is_alive=1
                        else:
                            logger.info(" thread  "+th.name+" is dead now !")
                            threads.remove(th)
                            
                if(is_alive==0):
                    
                    execute(job)
                    logger.info(" thread  "+job+" is working  now !")
            
            
        for api_job in configureRead.get_api_section():
            
            if(len(threads)==0):
                execute(api_job)
            else:
                is_alive=0
                for th in threads:
                    if(th.name==api_job):
                        
                        if(th.is_alive()):
                            logger.info(" thread  "+th.name+" is alive,so i'll do nothing for it!")
                            is_alive=1
                        else:
                            logger.info(" thread  "+th.name+" is dead now !")
                            threads.remove(th)
                           
                if(is_alive==0):
                    execute(api_job)
                    logger.info(" thread  "+api_job+" is working  now !")
                 
  
        time.sleep(int(configureRead.getCommonValue('concurrent', 'sleepTimeInMainThread')))
        
