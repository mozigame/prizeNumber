# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

import requests
import re
import codecs 
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
    
   


    res=requests.get(url=getJobValue('luckship','site_url'),headers=headers,timeout=300)
        

    page_element=etree.HTML(res.text)
    
    body_node=page_element.xpath('//div[starts-with(@class,"stagesResult")]')
    for node in body_node:
        left=node.xpath('./font/text()')
        print(left[0].replace('\xa0',''))
        right=node.xpath('./span/text()')[0].replace('\xa0',',')
       
        print(right[:-2])
                
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
    cf.read("job.conf")
    kvs  = cf.items(part)
    return kvs
def getJobValue(jobName,part):
    cf = configparser.ConfigParser()
    cf.readfp(codecs.open("job.conf", "r", "utf-8-sig"))
    #cf.read("job.conf")
    return cf.get(jobName, part)

handler()
