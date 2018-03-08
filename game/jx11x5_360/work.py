# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from  game.common import *
from model.Item import *
import re

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

        body_node=page_element.xpath('//div[@class="main"]/div[@class="tc_news_tc"]/div[@class="tc_dlc"]/table/tr')
        logger.info('jx11*5_360  '+'new spider enter and current max issue is :'+str(current_issue))
        
        for node in body_node:
           

            numbers=''
            if len(node.xpath('./td')[2].xpath('./table'))>0:
            #print(etree.tostring(node))
                tnode=node.xpath('./td')
                if(len(tnode)<3 or current_issue>=int(tnode[1].xpath('./text()')[0])):
                    continue
                
                for t in tnode[2].xpath('./table/tr/td[@class="kj_hm"]/text()'):
                    numbers=numbers+','+t
                numbers=numbers[1:]
                logger.info('jx11*5_360  '+"numbers :"+numbers)
                
                
                item =PrizeNumberItem()
                item.issue=tnode[1].xpath('./text()')[0].replace('-','')
                logger.info("new issue :"+item.issue)
                item.numbers=numbers
                
                item.ptime=tnode[0].xpath('./text()')[0]
                item.pdate=datetime.datetime.utcnow().strftime(date_format)
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
        logger.warn('jx11*5_360  '+' jx11*5_360  error for :'+" error:"+str(e))
        return items






