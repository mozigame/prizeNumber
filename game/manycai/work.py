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

logger = logging.getLogger("manycaiparser")

def handler(job_name='',prizeItem=[]):
    items=[]
    current_issue=0
    _list4api=spiderRecord4DB.getCurrentPrizeNumberFromDB4api(job_name)
    
    _current_item4api={}
    for item in _list4api:
        if('bj_pk10'==item[4]):
            _current_item4api[item[4]]=item[2]
        else:
            _current_item4api[item[4]]='20'+str(item[2])

    try:
        for url in configureRead.getApiNode(job_name):
            logger.info("code :"+url[0]+ " ,url:"+url[1])
            siteUrl=url[1]
            res=requests.get(url=siteUrl,headers=headers,timeout=300)
            if res:
                d=json.loads(res.text)
                logger.info('res :'+str(d))
                for j in d:
                    if('xg_lhc'==url[0]):
                        j['issue']='20'+j['issue'].('\/','')
                    elif('qq_ffc'==url[0]):
                        j['issue']=j['opendate'].replace('-','').replace(' ','').replace(':','')[2:-2]
                    if(_current_item4api.get(url[0])==None or int(j['issue'])>int(_current_item4api.get(url[0]))):
                        item =PrizeNumberItem()
                        if('bj_pk10'==url[0] or 'xg_lhc'==url[0] or 'qq_ffc'==url[0]):
                            item.issue=j['issue']
                        else:
                            item.issue=j['issue'][2:]
                        logger.info("new issue :"+item.issue)
                        if('xg_lhc'==url[0]):
                            item.numbers=j['code'].replace('+',',')
                        else:
                            item.numbers=j['code']
                        logger.info("origin:" + j['code'] + ",numbers :"+item.numbers)
                        item.ptime=j['opendate']
                        item.pdate=datetime.datetime.now().strftime(date_format)
                        item.source=url[1]
                        item.code=url[0]                      
                        item.update_time=int(round(time.time() * 1000))
                        item.name=configureRead.getJobValue(job_name,'name')
                        item.priority=configureRead.getJobValue(job_name,'priority')
                        item.job_name=job_name
                        item.status=1
                        logger.info("item content :" + item.printContent())
                        items.append(item)
                        
                        logger.info('end')
        items.sort(key=lambda item:item.issue, reverse=False)
        
        return items
        
    except Exception as e:
        logger.warn(' open cai error for :'+" error:"+str(e))
        return items






