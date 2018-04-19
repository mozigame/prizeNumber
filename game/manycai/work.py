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
        if('bj_pk10'==item[4] or 'qq_ffc'==item[4] or 'js_k3'==item[4] or 'gd_11x5'==item[4] or 'sd_11x5'==item[4] or 'bj_kl8'==item[4]):
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
                        j['issue']='20'+j['issue'].replace('/','')
                    elif('qq_ffc'==url[0]):
                        j['issue']=j['opendate'].replace('-','').replace(' ','').replace(':','')[2:-2]
                    elif('gd_11x5'==url[0] or 'jx_11x5'==url[0]):
                        j['issue']=j['issue'][:8]+j['issue'][9:]
                    elif('tj_ssc'==url[0]):
                        last=j['issue'][8:]
                        if(int(last)>0 and int(last)<10):
                            last='00'+last
                        elif(int(last)>=10 and int(last)<100):
                            last='0'+last
                        j['issue']=j['issue'][:8]+last
                    if(_current_item4api.get(url[0])==None or int(j['issue'])>int(_current_item4api.get(url[0]))):
                        item =PrizeNumberItem()
                        if('bj_pk10'==url[0] or 'xg_lhc'==url[0] or 'qq_ffc'==url[0] or 'js_k3'==url[0] or 'gd_11x5'==url[0] or 'sd_11x5'==url[0] or 'bj_kl8'==url[0]):
                            item.issue=j['issue']
                        else:
                            item.issue=j['issue'][2:]
                        logger.info("new issue :"+item.issue)
                        if('bj_pk10'==url[0] or 'xg_lhc'==url[0] or 'gd_11x5'==url[0] or 'sd_11x5'==url[0] or 'jx_11x5'==url[0]):
                            if('xg_lhc'==url[0]):
                                j['code']=j['code'].replace('+',',')
                            spilts=j['code'].split(",")
                            for i in range(len(spilts)):
                                if(int(spilts[i])<10):
                                    spilts[i]='0'+spilts[i]
                            item.numbers=','.join(spilts)
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
                        if('bj_kl8'==url[0]):
                            numbers=j['code']
                            numbersSpilt=numbers.split(',')
                            if len(numbersSpilt) == 20:
                                item_pcdd=PrizeNumberItem()
                                first=(int(numbersSpilt[0])+int(numbersSpilt[1])+int(numbersSpilt[2])+int(numbersSpilt[3])+int(numbersSpilt[4])+int(numbersSpilt[5]))%10
                                second=(int(numbersSpilt[6])+int(numbersSpilt[7])+int(numbersSpilt[8])+int(numbersSpilt[9])+int(numbersSpilt[10])+int(numbersSpilt[11]))%10
                                third=(int(numbersSpilt[12])+int(numbersSpilt[13])+int(numbersSpilt[14])+int(numbersSpilt[15])+int(numbersSpilt[16])+int(numbersSpilt[17]))%10
                                forth=first+second+third
                                item_pcdd.numbers = str(first) + ',' + str(second) + ',' + str(third) + ',' + str(forth)
                                item_pcdd.code='pc_dd'
                                item_pcdd.name='幸运28'
                                item_pcdd.issue=item.issue
                                item_pcdd.ptime=item.ptime
                                item_pcdd.pdate=item.pdate
                                item_pcdd.source=item.source
                                item_pcdd.update_time=item.update_time
                                item_pcdd.priority=item.priority
                                item_pcdd.job_name=item.job_name
                                item_pcdd.status=1
                                logger.info("item_pcdd content :" + item_pcdd.printContent())
                                items.append(item_pcdd)
                                item_ssc=PrizeNumberItem()
                                first=(int(numbersSpilt[0])+int(numbersSpilt[1])+int(numbersSpilt[2])+int(numbersSpilt[3]))%10
                                second=(int(numbersSpilt[4])+int(numbersSpilt[5])+int(numbersSpilt[6])+int(numbersSpilt[7]))%10
                                third=(int(numbersSpilt[8])+int(numbersSpilt[9])+int(numbersSpilt[10])+int(numbersSpilt[11]))%10
                                forth=(int(numbersSpilt[12])+int(numbersSpilt[13])+int(numbersSpilt[14])+int(numbersSpilt[15]))%10
                                fifth=(int(numbersSpilt[16])+int(numbersSpilt[17])+int(numbersSpilt[18])+int(numbersSpilt[19]))%10
                                item_ssc.numbers=str(first) + ',' + str(second) + ',' + str(third) + ',' + str(forth) + ',' + str(fifth)
                                item_ssc.code='bj_ssc'
                                item_ssc.name='北京时时彩'
                                item_ssc.issue=item.issue
                                item_ssc.ptime=item.ptime
                                item_ssc.pdate=item.pdate
                                item_ssc.source=item.source
                                item_ssc.update_time=item.update_time
                                item_ssc.priority=item.priority
                                item_ssc.job_name=item.job_name
                                item_ssc.status=1
                                logger.info("item_ssc content :" + item_ssc.printContent())
                                items.append(item_ssc)

        items.sort(key=lambda item:item.issue, reverse=False)
        
        return items
        
    except Exception as e:
        logger.warn(' open cai error for :'+" error:"+str(e))
        return items






