#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from urllib import request
from hf.view.getConfig import getHfSigRsAddress
def autographsuccess(idCardNo,phoneNumber):

    req=createClient(idCardNo,phoneNumber)
    return req


def createClient(idCardNo,phoneNumber):
    url = getHfSigRsAddress()
    params = {
        "id_card_no": idCardNo,
        "phone_number": phoneNumber,
        "result":1,
        "url":"https://asdfsdfjasd.e-shebao.com/upload/20200316/AAYoAAAIcCAYAAADoqen2003160946220_sign.jpg"
    }
    params = json.dumps(params)
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
    # 用bytes函数转换为字节
    params = bytes(params, 'utf8')

    req = request.Request(url=url, data=params, headers=headers, method='POST')
    response = request.urlopen(req).read().decode()
    return json.loads(response)
