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
    current_date=''

    if len(prizeItem)>0:
        current_date=prizeItem[0][1]
        current_issue=prizeItem[0][2]


    try:
        res=requests.get(url=configureRead.getJobValue(job_name,'site_url'),headers=headers,timeout=300)


        page_element=etree.HTML(res.text)

        t_time_node=page_element.xpath('//div[@class="wrap"]/div[@class="chart-sc"]/div[@class="fl"]/strong[@class="red"]/text()')

        t_time=re.sub("\D", "", t_time_node[0])

        current_date_value=str(current_date).replace('-','')

        if t_time!=current_date_value:
            current_issue=0


        body_node=page_element.xpath('//td[@class="his-top"]/table/tbody/tr')

        for node in body_node:
            if node.xpath('./td[@class="blue"]/em[@class="orange"]/text()'):
                issue=(node.xpath('./td[@class="gray"]/text()')[0])
                if int(issue)>current_issue:
                    span=node.xpath('./td[@class="blue"]/em[@class="orange"]/text()')[0]
                    numbers=span.replace(' ',',')
                    span=node.xpath('./td[@class="blue"]/em[@class="blue"]/text()')[0]
                    numbers+=','+span.replace(' ',',')
                    item =PrizeNumberItem()
                    item.issue=issue
                    item.numbers=numbers
                    item.ptime=t_time
                    item.pdate=t_time
                    item.source=configureRead.getJobValue(job_name,'site_url')
                    item.code=configureRead.getJobValue(job_name,'code')
                    item.update_time=datetime.datetime.utcnow().strftime(UTC_FORMAT)
                    item.name=configureRead.getJobValue(job_name,'name')
                    item.priority=configureRead.getJobValue(job_name,'priority')
                    item.job_name=job_name
                    item.status=1
                    item.printContent()
                    items.append(item)

        items.sort(key=lambda item:item.issue, reverse=False)
        return items
    except Exception as e:
        print(str(e))
        return items






