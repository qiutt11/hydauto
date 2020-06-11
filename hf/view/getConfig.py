#! /usr/bin/env python
# -*- coding:utf8 -*-
from configparser import ConfigParser

def getHost():
    cp = ConfigParser()
    # 以.cfg结尾的配置文件
    cp.read('E:\python\psp\hf\config.cfg',encoding="UTF-8")
    # 获取mysql中的host值
    host = str(cp.get('hfmysql', 'host'))
    print(host)
    return host
def getUser():
    cp = ConfigParser()
    # 以.cfg结尾的配置文件
    cp.read('E:\python\psp\hf\config.cfg',encoding="UTF-8")
    # 获取mysql中的user值
    user = str(cp.get('hfmysql', 'user'))
    print(user)
    return user
def getPasswd():
    cp = ConfigParser()
    # 以.cfg结尾的配置文件
    cp.read('E:\python\psp\hf\config.cfg',encoding="UTF-8")
    # 获取mysql中的passwd值
    passwd = str(cp.get('hfmysql', 'passwd'))
    print(passwd)
    return passwd
def getDb():
    cp = ConfigParser()
    # 以.cfg结尾的配置文件
    cp.read('E:\python\psp\hf\config.cfg',encoding="UTF-8")
    # 获取mysql中的db值
    db = str(cp.get('hfmysql', 'db'))
    print(db)
    return db

def getHfSigRsAddress():
    cp = ConfigParser()
    # 以.cfg结尾的配置文件
    cp.read('E:\python\psp\hf\config.cfg',encoding="UTF-8")
    # 获取hfsignatureResult中的address值
    address = str(cp.get('hfsResult', 'address'))
    print(address)
    return address
def getHfSignManualResult():
    cp = ConfigParser()
    # 以.cfg结尾的配置文件
    cp.read('E:\python\psp\hf\config.cfg',encoding="UTF-8")
    # 获取hfsignManualExamine中的address值
    address = str(cp.get('hfsManualExamine', 'address'))
    print(address)
    return address
def getHfWithDrawManualResult():
    cp = ConfigParser()
    # 以.cfg结尾的配置文件
    cp.read('E:\python\psp\hf\config.cfg',encoding="UTF-8")
    # 获取hfsManualWithDrawal中的address值
    address = str(cp.get('hfsManualWithDrawal', 'address'))
    print(address)
    return address