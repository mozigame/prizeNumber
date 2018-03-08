# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from  game.common import *
from model.Item import *


def handler(job_name='',prizeItem=[]):
    items=[]
    current_issue=0
    #current_date=yesterday

    if len(prizeItem)>0:
        current_date=prizeItem[0][1]
        current_issue=prizeItem[0][2]

    try:
        res=requests.get(url=configureRead.getJobValue(job_name,'site_url'),headers=headers,timeout=300)


        pageElement=etree.HTML(res.text)

        bodyNode=pageElement.xpath('//div[@class="lott_cont"]/table[1]/tr')

        for node in bodyNode:
            a=node.xpath('./td/text()')
            if len(a)>2 and int(a[0])>current_issue:
                item =PrizeNumberItem()
                item.issue=a[0]
                item.numbers=a[1]+','+a[2]
                item.ptime=a[3]
                item.pdate=datetime.datetime.utcnow().strftime(date_format)
                item.source=configureRead.getJobValue(job_name,'site_url')
                item.code=configureRead.getJobValue(job_name,'code')
                item.update_time=datetime.datetime.utcnow().strftime(UTC_FORMAT)
                item.name=configureRead.getJobValue(job_name,'name')
                item.job_name=job_name
                item.status=1
                item.printContent()
                items.append(item)

        items.sort(key=lambda item:item.issue, reverse=False)
        return items
    except Exception as e:
        print(str(e))
