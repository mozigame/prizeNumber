# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from  game.common import *
from model.Item import *
import re

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
        body_node=page_element.xpath('//div[@class="lott_cont"]/table[1]/tr/td/text()')
        issue_node=page_element.xpath('//div[@class="lott_cont"]/text()')[0].strip()
        issue=re.sub("\D", "", issue_node)
        print(issue)
        numbers=''
        for node in body_node:
            numbers=numbers+','+node
        print(numbers[1:])

        if len(issue)>2 and int(issue)>current_issue:
            item =PrizeNumberItem()
            item.issue=issue
            item.numbers=numbers[1:]
            item.ptime=datetime.datetime.utcnow().strftime(date_format)
            item.pdate=datetime.datetime.utcnow().strftime(date_format)
            item.source=configureRead.getJobValue(job_name,'site_url')
            item.code=configureRead.getJobValue(job_name,'code')
            item.update_time=datetime.datetime.utcnow().strftime(UTC_FORMAT)
            item.name=configureRead.getJobValue(job_name,'name')
            item.job_name=job_name
            item.status=1
            item.printContent()
            items.append(item)

        return items
    except Exception as e:
        print(str(e))
        return items
