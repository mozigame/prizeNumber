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

        body_node=page_element.xpath('//tbody[@id="data-tab"]/tr')
        
        logger.info('cqssc_360  '+'new spider enter and current max issue is :'+str(current_issue))
        
        for node in body_node:
            a=node.xpath('./td/text()')

            numbers=''
            if not a:
                continue
            
            if len(a)>2 and  int(a[0].replace('-',''))>current_issue:

                span=node.xpath('./td/span/text()')
                if not span:
                    continue
                number_tmp=span[0]
                logger.info('length :'+str(len(number_tmp)))
                for t in number_tmp:
                    numbers=numbers+','+t
                    
                logger.info('cqssc_360  '+'number :'+numbers)
                strong=node.xpath('./td/span/strong/text()')
                stringNumber=strong[0]

                numbers=numbers[1:]+','+stringNumber

                item =PrizeNumberItem()
                item.issue=a[0].replace('-','')
                logger.info("new issue :"+item.issue)
                item.numbers=numbers
                if len(a[1]) > 4:
                    item.ptime=a[1][:-3]
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
        logger.warn('cqssc_360  '+' cqssc_360  error for :'+" error:"+str(e))
        return items