# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

import requests
import re
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
siteUrl='http://chart.cp.360.cn/kaijiang/syy?sb_spm=2358cfaace452d28490f4dc4ac6ce383'

def handler():

    res=requests.get(url=siteUrl,headers=headers,timeout=300)


    page_element=etree.HTML(res.text)
    t_time=page_element.xpath('//div[@class="wrap"]/div[@class="chart-sc"]/div[@class="fl"]/strong[@class="red"]/text()')
    print(t_time)
    issue=re.sub("\D", "", t_time[0])
    print(issue)
    body_node=page_element.xpath('//td[@class="his-top"]/table/tbody/tr')

    for node in body_node:
        #print(etree.tostring(node))/strong[@class="red"]
        if node.xpath('./td[@class="blue"]/em[@class="orange"]/text()'):
            print(node.xpath('./td[@class="gray"]/text()')[0])
            print(node.xpath('./td[@class="blue"]/em[@class="orange"]/text()')[0])
            print(node.xpath('./td[@class="blue"]/em[@class="blue"]/text()')[0])
        #date1=node.xpath('./td/text()')

        #print(date1[0] +' '+date1[1])
        #span=node.xpath('./td/span/text()')
        #for s in span:
           # print(s)
        #print(etree.tostring(node))




handler()
