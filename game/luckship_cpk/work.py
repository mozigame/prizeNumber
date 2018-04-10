# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from  game.common import *
from model.Item import *


logger = logging.getLogger("spiderparser")



def handler(job_name='',prizeItem=[]):
    items=[]
    current_issue=0
    #current_date=yesterday
    
    if len(prizeItem)>0:
        current_date=prizeItem[0][1]
        current_issue=prizeItem[0][2]



    try:
        res=requests.get(url=configureRead.getJobValue(job_name,'site_url'),headers=headers,timeout=300)
        

        page_element=etree.HTML(res.text)

        body_node=page_element.xpath('//div[starts-with(@class,"stagesResult")]')
        
        logger.info('luckship  '+'new spider enter and current max issue is :'+str(current_issue))
        for node in body_node:
            a=node.xpath('./font/text()')

            numbers=''
            if not a:
                continue
            
            if   int(a[0].replace('\xa0',''))>current_issue:

                span=node.xpath('./span/text()')[0].replace('\xa0',',')
                if not span:
                    continue
                
                numbers=span[:-2]
                    
                logger.info('luckship  '+'number :'+numbers)
                
                item =PrizeNumberItem()
                item.issue=a[0].replace('\xa0','')
                item.numbers=numbers
                
                item.pdate=datetime.datetime.now().strftime(date_format)
                item.source=configureRead.getJobValue(job_name,'site_url')
                item.code=configureRead.getJobValue(job_name,'code')
                item.update_time=int(round(time.time() * 1000))
                item.name=configureRead.getJobValue(job_name,'name')
                item.priority=configureRead.getJobValue(job_name,'priority')
                item.job_name=job_name
                item.status=1
                logger.info("item content :")
                        
                logger.info(item.printContent())
                items.append(item)

        items.sort(key=lambda item:item.issue, reverse=False)
        return items
    except Exception as e:
        logger.warn('luckship  '+' luckship  error for :'+" error:"+str(e))
        return items