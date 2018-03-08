# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

import requests
import re
from lxml import etree
import sys
import datetime
import time
import configparser
sys.path.append("../..")
import json
from   utils import configureRead

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
siteUrl='http://www.gdhpv.com/draw-center-service/resources/external/drawRecords/CQSSC?page=0&size=10'

def handler():
    
   


    for url in getApiNode('gdhpv'):
        print(url[0])
        print(url[1])
        
        
        siteUrl=url[1]
        res=requests.get(url=siteUrl,headers=headers,timeout=300)
        if res:
            d=json.loads(res.text)
        #json.dumps(data2,sort_keys=True)
        #print(context[0])
        
        
            print(d)
            for j in d:
                print(j)
                print(j['numeroNo'].replace('_',''))
                print(j['winNo'])
                print(j['winTime'])
                
        #print(context['data'])
        
        
        #html = urllib2.urlopen(r'http://api.douban.com/v2/book/isbn/9787218087351')

#hjson = json.loads(heml.read())

    ##page_element=etree.HTML(res.text)
    #t_time=page_element.xpath('//div[@class="main"]/div[@class="tc_news_tc"]/div[@class="tc_dlc"]/table/tbody/text()')
    #print(t_time)
    #issue=re.sub("\D", "", t_time[0])
    #print(issue)
    #body_node=page_element.xpath('//div[@class="main"]/div[@class="tc_news_tc"]/div[@class="tc_dlc"]/table/tr')
    
    
        #print(date1[0] +' '+date1[1])
        #span=node.xpath('./td/span/text()')
        #for s in span:
           # print(s)
        #print(etree.tostring(node))


def getApiNode(part):
    cf = configparser.ConfigParser()
    cf.read("api.conf")
    kvs  = cf.items(part)
    return kvs

handler()
