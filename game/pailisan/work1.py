# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

import requests
import re
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
siteUrl='http://chart.cp.360.cn/kaijiang/p3?sb_spm=d135150d6ec62fd1e3b9c4708478c60e'

def handler():

    res=requests.get(url=siteUrl,headers=headers,timeout=300)


    pageElement=etree.HTML(res.text)

    bodyNode=pageElement.xpath('//tbody[@id="data-tab"]/tr')

    for node in bodyNode:
        date1=node.xpath('./td/text()')

        print(date1[0] +' '+date1[1])
        span=node.xpath('./td/span/text()')
        for s in span:
            print(s)
        #print(etree.tostring(node))




handler()
