# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''
from email.mime.text import MIMEText 
from  store import configureRead
import smtplib
import logging
import logging.config
import codecs
import yaml 
logging.config.dictConfig(yaml.load(codecs.open("conf/logger.yml", 'r', 'utf-8').read()))
logger = logging.getLogger("commonsparser")  
  
#===============================================================================  
# 要发给谁，这里发给2个人  
#===============================================================================  
mailto_list=configureRead.getCommonValue('mail', 'mail_list')
  
#===============================================================================  
# 设置服务器，用户名、口令以及邮箱的后缀  
#===============================================================================  
mail_host=configureRead.getCommonValue('mail', 'mail_host') 
mail_user=configureRead.getCommonValue('mail', 'mail_user')
mail_pass=configureRead.getCommonValue('mail', 'mail_pass')
mail_postfix=configureRead.getCommonValue('mail', 'mail_postfix') 
mail_from=configureRead.getCommonValue('mail', 'mail_from') 
mail_subject=configureRead.getCommonValue('mail', 'mail_subject')
 

  
#===============================================================================  
# 发送邮件  
#===============================================================================  
def send_mail(to_list,sub,content):  
    ''''' 
    to_list:发给谁 
    sub:主题 
    content:内容 
    send_mail("aaa@126.com","sub","content") 
    '''  
    me=mail_from+"<"+mail_from+"@"+mail_postfix+">"  
    msg = MIMEText(content)  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = to_list.replace(',',';') 
    print (to_list)
    try:  
        s = smtplib.SMTP_SSL(mail_host,port=465) 
        #s.connect(mail_host)  
        s.login(mail_user,mail_pass)  
        s.sendmail(me, to_list, msg.as_string())  
        s.close()  
        return True  
    except Exception  as e:
        print (str(e) )
        return False  

def handler(sitedName,id,currentTime,scanLength,successLength,firstHintTime,secondHintTime,notThisDayTime,exceptList):
    if(successLength==0):
        sub=mail_subject+' '+sitedName
        
        content='spider id :'+str(id)+' time :'+str(currentTime)+" , scanLenth : "+str(scanLength)+" ,successLength :"+str(successLength)+" ,firstHintTime :"+str(firstHintTime)+" ,secondHintTime :"+str(secondHintTime)+" ,notThisDayCount :"+str(notThisDayTime)+":\n\n"
        
        for ex in exceptList:
            content=content+ex.Type+" "+ex.URL+" "+ex.Message+" "+ex.Desc +"\n"
        send_mail(mailto_list,sub,content)