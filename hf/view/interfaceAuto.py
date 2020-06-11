#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
from suds.client import Client

def createClient():
    url = 'http://118.26.173.72:8094/psp/hf/notify/signature/result'
    params = {
        "id_card_no": getRandomBusinessId(),
        "phone_number": "2"
    }
    params = json.dumps(params)
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json',
               "host": '10.100.19.168'}
    # 用bytes函数转换为字节
    params = bytes(params, 'utf8')

    req = request.Request(url=url, data=params, headers=headers, method='POST')
















