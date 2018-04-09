# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from  game.common import *
from model.Item import *
from store import spiderRecord4DB
import re
import json

logger = logging.getLogger("bccaiparser")

def handler(job_name='',prizeItem=[]):
    items=[]
    current_issue=0
    _list4api=spiderRecord4DB.getCurrentPrizeNumberFromDB4api(job_name)
    
    _current_item4api={}
    for item in _list4api:
        _current_item4api[item[4]]=item[2]

    try:
        for url in configureRead.getApiNode(job_name):
            logger.info("code :"+url[0]+ " ,url:"+url[1])
        
            siteUrl=url[1]
            res=requests.get(url=siteUrl,headers=headers,timeout=300)
            if res:
                logger.info('res :'+str(res))
                logger.info('current issue is :'+str(_current_item4api.get(url[0])))
                d=json.loads(res.text)
                if d["code"]==0:
                    for j in d["data"]:
                        if(_current_item4api.get(url[0])==None or int(j['resultNum'])>int(_current_item4api.get(url[0]))):
                            item =PrizeNumberItem()
                            item.issue=j['resultNum']
                            logger.info("new issue :"+item.issue)
                            if(j['result']!=None and not j['result'].strip()):
                                item.numbers=j['result']
                                logger.info("issue:" + item.issue + ",numbers :"+item.numbers)
                                item.ptime=j['timeFormat']
                                item.pdate=datetime.datetime.utcnow().strftime(date_format)
                                item.source=url[1]
                                item.code=url[0]
                                item.update_time=int(round(time.time() * 1000))
                                item.name=configureRead.getJobValue(job_name,'name')
                                item.priority=configureRead.getJobValue(job_name,'priority')
                                item.job_name=job_name
                                item.status=1
                                logger.info("item content :")
                                logger.info(item.printContent())
                                items.append(item)
                                logger.info('end')
        items.sort(key=lambda item:item.issue, reverse=False)
        return items
        
    except Exception as e:
        logger.warn(' bccai error for :'+" error:"+str(e))
        return items






