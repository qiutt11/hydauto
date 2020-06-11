#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
from hf.view.getConfig import getHost,getUser,getPasswd,getDb
def createDbCon():
    host=getHost()
    user=getUser()
    passwd=getPasswd()
    db=getDb()
    db = pymysql.connect(host,user,passwd,db, charset='utf8')
    cursor = db.cursor()
    return cursor
