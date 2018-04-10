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

logger = logging.getLogger("opencaiparser")

def handler(job_name='',prizeItem=[]):
    items=[]
    current_issue=0
    #current_date=yesterday
    _list4api=spiderRecord4DB.getCurrentPrizeNumberFromDB4api(job_name)
    
    _current_item4api={}
    for item in _list4api:
        #print(item[2])
        if('bj_pk10'==item[4]  or 'xg_lhc'==item[4] or 'luckship'==item[4] or 'bj_ssc'==item[4] or 'tw_ssc'==item[4]):
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
        
        
                #print(d)
                logger.info('res :'+str(d))
                logger.info('current issue is :'+str(_current_item4api.get(url[0])))
                for j in d["data"]:
                
                    
                    if(_current_item4api.get(url[0])==None or int(j['expect'])>int(_current_item4api.get(url[0]))):
                    
                        
                        #print(j['opentimestamp'])
                    
                        item =PrizeNumberItem()
                        if('bj_pk10'==url[0] or 'xg_lhc'==url[0]  or 'luckship'==url[0] or 'bj_ssc'==url[0] or 'tw_ssc'==url[0]):
                            item.issue=j['expect']
                        else:
                            item.issue=j['expect'][2:]
                        logger.info("new issue :"+item.issue)
                        if('bj_ssc'==url[0] or 'tw_ssc'==url[0]):
                            numbers=j['opencode'][:-3]
                            numbersSpilt=numbers.split(',')
                            if len(numbersSpilt) == 20:
                                first=(int(numbersSpilt[0])+int(numbersSpilt[1])+int(numbersSpilt[2])+int(numbersSpilt[3]))%10
                                second=(int(numbersSpilt[4])+int(numbersSpilt[5])+int(numbersSpilt[6])+int(numbersSpilt[7]))%10
                                third=(int(numbersSpilt[8])+int(numbersSpilt[9])+int(numbersSpilt[10])+int(numbersSpilt[11]))%10
                                forth=(int(numbersSpilt[12])+int(numbersSpilt[13])+int(numbersSpilt[14])+int(numbersSpilt[15]))%10
                                fifth=(int(numbersSpilt[16])+int(numbersSpilt[17])+int(numbersSpilt[18])+int(numbersSpilt[19]))%10
                                numbers=str(first) + ',' + str(second) + ',' + str(third) + ',' + str(forth) + ',' + str(fifth)
                                item.numbers=numbers
                        else:
                            item.numbers=j['opencode'].replace('+',',')
                        logger.info("origin:" + j['opencode'] + ",numbers :"+item.numbers)
                        item.ptime=j['opentime']
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
                        
                        logger.info('end')

                        if('bj_ssc'==url[0]):
                            numbers=j['opencode'][:-3]
                            numbersSpilt=numbers.split(',')
                            if len(numbersSpilt) == 20:
                                first=(int(numbersSpilt[0])+int(numbersSpilt[1])+int(numbersSpilt[2])+int(numbersSpilt[3])+int(numbersSpilt[4])+int(numbersSpilt[5]))%10
                                second=(int(numbersSpilt[6])+int(numbersSpilt[7])+int(numbersSpilt[8])+int(numbersSpilt[9])+int(numbersSpilt[10])+int(numbersSpilt[11]))%10
                                third=(int(numbersSpilt[12])+int(numbersSpilt[13])+int(numbersSpilt[14])+int(numbersSpilt[15])+int(numbersSpilt[16])+int(numbersSpilt[17]))%10
                                forth=first+second+third
                                numbers = str(first) + ',' + str(second) + ',' + str(third) + ',' + str(forth)
                                item_pc =PrizeNumberItem()
                                item_pc.issue=item.issue
                                logger.info("new issue :"+item_pc.issue)
                                item_pc.numbers=numbers
                                logger.info("origin:" + j['opencode'] + ",numbers :"+item_pc.numbers)
                                item_pc.ptime=item.ptime
                                item_pc.pdate=item.pdate
                                item_pc.source=item.source
                                item_pc.code='pc_dd'
                                item_pc.update_time=item.update_time
                                item_pc.name='pc蛋蛋'
                                item_pc.priority=item.priority
                                item_pc.job_name=item.job_name
                                item_pc.status=1
                                logger.info("item_pc content :")
                                logger.info(item_pc.printContent())
                                items.append(item_pc)

        items.sort(key=lambda item:item.issue, reverse=False)
        
        return items
        
    except Exception as e:
        logger.warn(' open cai error for :'+" error:"+str(e))
        return items






