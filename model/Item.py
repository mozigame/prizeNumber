'''
Created on 2017年4月6日

@author: shawn
'''


class PrizeNumberItem():
    def __init__(self, pdate='', issue='', numbers='',priority='', name='', ptime='', _code='', source='', update_time='',job_name='',status=''):
        self.pdate = pdate
        self.issue = issue
        self.numbers = numbers
        self.ptime = ptime
        self.source = source
        self.update_time = update_time
        self.code = _code
        self.name = name
        self.job_name=job_name
        self.status=status
        self.priority=priority

    def printContent(self):
        
        content='pdate :'+self.pdate+' issue :'+self.issue+" numbers :"+self.numbers+' ptime : '+self.ptime+ '  source :'+self.source+' code:'+self.code+" name :"+self.name
        #content='aa'
        #print(content)
        return content


class job_detail():
    def __init__(self, url='', _type='', message='', desc=''):
        self.url = url


class ItemSpiderExcept():
    def __init__(self, url='', _type='', message='', desc=''):
        self.URL = url
        self.Type = _type
        self.Message = message
        self.Desc = desc
