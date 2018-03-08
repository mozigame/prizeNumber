# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''
import configparser
import codecs 
local='online'
#local='test'
#local='local'

def getCommonValue(siteName,part):
    cf = configparser.ConfigParser()
    
    cf.read("conf/"+local+"/common.conf")
    
    return cf.get(siteName, part)

def getDBValue(siteName,part):
    cf = configparser.ConfigParser()
    
    cf.read("conf/"+local+"/db.conf")
    return cf.get(siteName, part)
def getJobValue(jobName,part):
    cf = configparser.ConfigParser()
    cf.readfp(codecs.open("conf/job.conf", "r", "utf-8-sig"))
    #cf.read("job.conf")
    return cf.get(jobName, part)


    
def getNode(part):
    cf = configparser.ConfigParser()
    cf.read("job.conf")
    kvs  = cf.items(part)
    return kvs

def getApiNode(part):
    cf = configparser.ConfigParser()
    cf.read("conf/api.conf")
    kvs  = cf.items(part)
    return kvs

def get_section():
    cf = configparser.ConfigParser()
    cf.readfp(codecs.open("conf/job.conf", "r", "utf-8-sig"))
    return cf.sections()

def get_api_section():
    cf = configparser.ConfigParser()
    cf.readfp(codecs.open("conf/api.conf", "r", "utf-8-sig"))
    return cf.sections()




