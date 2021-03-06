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

logger = logging.getLogger("gdhpvparser")


def handler(job_name='',prizeItem=[]):
    items=[]
    current_issue=0
    #current_date=yesterday
    _list4api=spiderRecord4DB.getCurrentPrizeNumberFromDB4api(job_name)
    
    _current_item4api={}
    for item in _list4api:
        #print(item[2])
        if('bj_pk10'==item[4] or 'xg_lhc'==item[4] or 'luckship'==item[4] or 'bj_ssc'==item[4] or 'tw_ssc'==item[4] or 'pc_dd'==item[4]):
            _current_item4api[item[4]]=item[2]
        else:
            _current_item4api[item[4]]='20'+str(item[2])
        
        
    
    #print(_current_item4api)
        
    
    
    



    try:
        for url in configureRead.getApiNode(job_name):
            logger.info("code :"+url[0]+ " ,url:"+url[1]) 
        
        
            siteUrl=url[1]
            res=requests.get(url=siteUrl,headers=headers,timeout=300)
            if res:
                d=json.loads(res.text)
        #json.dumps(data2,sort_keys=True)
        #print(context[0])
        
        
                logger.info('res :'+str(d))
                logger.info('current issue is :'+str(_current_item4api.get(url[0])))
                for j in d:
                
                    logger.info("issue :"+j['numeroNo'])
                    logger.info("current issue :"+str(_current_item4api.get(url[0])))
                    if(_current_item4api.get(url[0])==None or int(j['numeroNo'].replace('-',''))>int(_current_item4api.get(url[0]))):
                        
                        
                        #print(j['opentimestamp'])
                        numbers=''
                        item =PrizeNumberItem()
                        if('bj_pk10'==url[0] or 'xg_lhc'==url[0] or 'luckship'==url[0] or 'bj_ssc'==url[0] or 'tw_ssc'==url[0] or 'pc_dd'==url[0]):
                            item.issue=j['numeroNo'].replace('-','')
                        else:
                            item.issue=j['numeroNo'].replace('-','')[2:]
                        logger.info("new issue :"+item.issue)
                        
                        if ('ah_k3'==url[0] or 'hub_k3'==url[0] or 'sh_k3'==url[0]  or 'js_k3'==url[0] or 'cq_ssc'==url[0] or 'tj_ssc'==url[0] or 'xj_ssc'==url[0] or 'bj_ssc'==url[0] or 'tw_ssc'==url[0]):
                            
                            for t in j['winNo']:
                                numbers=numbers+','+t
                        
                            item.numbers=numbers[1:]
                        elif ('pc_dd'==url[0]):
                            numbersSpilt=j['winNo'].split(',')
                            tema=int(numbersSpilt[0])+int(numbersSpilt[1])+int(numbersSpilt[2])
                            item.numbers=j['winNo'] + ',' + str(tema)
                        else:
                            item.numbers=j['winNo']
                        logger.info("numbers :"+item.numbers)
                        item.ptime=j['winTime']
                        item.pdate=datetime.datetime.now().strftime(date_format)
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
                        
                        logger.info("end ")

        items.sort(key=lambda item:item.issue, reverse=False)
        return items
        
    except Exception as e:
        logger.warn(' gdhpv  error for :'+" error:"+str(e))
        
        return items






