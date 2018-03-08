# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

import pymysql
from utils import configureRead

class MySQLDB():
    error_code = ''
    _instance = None
    _conn = None
    _cur = None
    _TIMEOUT = 30
    _timecount = 0
    

    def __init__(self,db_name):
        self.db_name=db_name
        host_value=configureRead.getDBValue(self.db_name, 'db_host')
        port_value=int(configureRead.getDBValue(self.db_name, 'db_port'))
        db_name_value=configureRead.getDBValue(self.db_name, 'db_name')
        user_value=configureRead.getDBValue(self.db_name, 'db_user')
        pass_value=configureRead.getDBValue(self.db_name, 'db_pass')
        charsetValue=configureRead.getDBValue(self.db_name, 'db_charset')
        self._conn = pymysql.connect(host=host_value,
                                     port=port_value,
                                     user=user_value,
                                     passwd=pass_value,
                                     db=db_name_value,
                                     charset='utf8'
                                     #charset=charsetValue
                                     )

        self._cur = self._conn.cursor()
        #db.set_character_set('utf8')
        #self._instance = MySQLdb

    def show(self):

        cur = self.conn.cursor()

        sql = "select * from person"

        cur.execute(sql)

        rows = cur.fetchall()

        # print(rows)

        for dr in rows:
            print(dr)

    def query(self, sql):
        self._cur.execute("SET NAMES utf8")
        result = self._cur.execute(sql)
        return result

    def queryWithArgs(self, sql):
        self._cur.execute("SET NAMES utf8")
        result = self._cur.execute(sql)
        return result

    def update(self, sql):
        try:
            self._cur.execute("SET NAMES utf8")
            result = self._cur.execute(sql)
            self._conn.commit()
        except pymysql.err as e:
            self.error_code = e.args[0]
        result = False
        return result

    def insert(self, sql):
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.execute('SET CHARACTER SET utf8;')
            self._cur.execute('SET character_set_connection=utf8;')

            self._cur.execute(sql)
            id = self._conn.insert_id()
            self._conn.commit()

            return id
        except pymysql.err as e:

            self.error_code = e.args[0]
        return False

    def batchInsert(self, sql, items):
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.executemany(sql, items)
            self._conn.commit()

        except pymysql.err as e:

            self.error_code = e.args[0]
        return False

    def fetchAllRows(self):

        return self._cur.fetchall()

    def fetchOneRow(self):
        return self._cur.fetchone()

    def getRowCount(self):

        return self._cur.rowcount

    def commit(self):

        self._conn.commit()

    def rollback(self):

        self._conn.rollback()

    def __del__(self):

        try:
            self._cur.close()
            self._conn.close()
        except:
            pass

    def close(self):
        u'关闭数据库连接'
        self.__del__()

if __name__ == '__main__':
    db = MySQLDB()
    db.show()
