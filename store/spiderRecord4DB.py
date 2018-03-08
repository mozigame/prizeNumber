# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from utils.mysql import *


def getCurrentPrizeNumberFromDB(jobName):
    db = MySQLDB('job')
    
    sql = "select  id,pdate,issue,numbers,code,name,job_name,priority from PrizeNumberItem where id in(SELECT max(id) from PrizeNumberItem where job_name='"+jobName+"');"
    db.query(sql);
    result = db.fetchAllRows();
    db.close()
    return result

def getCurrentPrizeNumberFromDB4api(apiName):
    db = MySQLDB('job')
    sql = "select  id,pdate,issue,numbers,code,name,job_name,priority from PrizeNumberItem where id in (select max(id) from PrizeNumberItem where job_name= '"+apiName+"' group by code );"
    db.query(sql);
    result = db.fetchAllRows();
    db.close()
    return result

def get_recent_item(code,issue):
    db = MySQLDB('job')
    sql = "select  id,pdate,issue,numbers,code,name,job_name,priority from PrizeNumberItem where id in (select min(id) from PrizeNumberItem where   issue="+issue+" and code= '"+code+"' group by job_name );"
    db.query(sql);
    result = db.fetchAllRows();
    db.close()
    return result
def batchInsert(items):
    
    db = MySQLDB('job')
    sql='insert into PrizeNumberItem(pdate,issue,numbers,ptime,source,update_time,code,name,job_name,status,priority) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    tmpItem=[]
    for e in items:
        tmpItem.append((e.pdate,e.issue,e.numbers,e.ptime,e.source,e.update_time,e.code,e.name,e.job_name,e.status,e.priority))
    db.batchInsert(sql,tmpItem)
    db.close()
    
def batchUpdate(items):
    
    db = MySQLDB('lottery')
    sql='update lp_prize_number_item set numbers=%s,update_time=%s,spride_number_catch_time=%s where code=%s and issue_alias=%s'
    tmpItem=[]
   
    for e in items:
        if('x' in e.numbers):
            continue
        tmpItem.append((e.numbers,e.update_time,e.update_time,e.code,e.issue))
    db.batchInsert(sql,tmpItem)
    db.close()    
    
    



