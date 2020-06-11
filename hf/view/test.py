#! /usr/bin/env python
# -*- coding:utf8 -*-
from configparser import ConfigParser

def getHost():
    cp = ConfigParser()
    # 以.cfg结尾的配置文件
    cp.read('E:\python\psp\hf\config.cfg')
    # 获取mysql中的host值
    host = str(cp.get('mysql', 'host'))
    print(host)
    return host




if __name__ == '__main__':
    getHost()
