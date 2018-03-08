# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

import requests
import re
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
siteUrl='http://www.jxlottery.cn/dlc.php'

def handler():

    res=requests.get(url=siteUrl,headers=headers,timeout=300)


    page_element=etree.HTML(res.text)
    #t_time=page_element.xpath('//div[@class="main"]/div[@class="tc_news_tc"]/div[@class="tc_dlc"]/table/tbody/text()')
    #print(t_time)
    #issue=re.sub("\D", "", t_time[0])
    #print(issue)
    body_node=page_element.xpath('//div[@class="main"]/div[@class="tc_news_tc"]/div[@class="tc_dlc"]/table/tr')
    
    for node in body_node:
        #print(etree.tostring(node))/strong[@class="red"]
        #print(etree.tostring(node))
        numbers=''
        if len(node.xpath('./td')[2].xpath('./table'))>0:
            #print(etree.tostring(node))
            tnode=node.xpath('./td')
            if(len(tnode)<3):
                continue
            print(tnode[0].xpath('./text()')[0])
            print(tnode[1].xpath('./text()')[0])
            for t in tnode[2].xpath('./table/tr/td[@class="kj_hm"]/text()'):
                numbers=numbers+','+t
            numbers=numbers[1:]
            print(numbers)
            #print(node.xpath('./td[@class="blue"]/em[@class="orange"]/text()')[0])
            #print(node.xpath('./td[@class="blue"]/em[@class="blue"]/text()')[0])
        #date1=node.xpath('./td/text()')

        #print(date1[0] +' '+date1[1])
        #span=node.xpath('./td/span/text()')
        #for s in span:
           # print(s)
        #print(etree.tostring(node))




handler()
