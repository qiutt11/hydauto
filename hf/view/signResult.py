#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from urllib import request
from hf.view.getConfig import getHfSignManualResult
def resultSuccess(idCardNo,result):

    url = getHfSignManualResult()
    params = {
        "id_card_no": idCardNo,
        "result": result,
        "reason":"成功",
        "contract_pdf_url":"https://asdfsdfjasd.e-shebao.com/upload/pdfhetong/qt/411528199404087010_ht.pdf"
    }
    params = json.dumps(params)
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json',
               "host": '118.26.173.72'}
    # 用bytes函数转换为字节
    params = bytes(params, 'utf8')

    req = request.Request(url=url, data=params, headers=headers, method='POST')
    response = request.urlopen(req).read().decode()
    return json.loads(response)

def resultFalse(idCardNo,result):

    url = getHfSignManualResult()
    params = {
        "id_card_no": idCardNo,
        "result": result,
        "reason":"身份证照片不清晰",
        "contract_pdf_url":"https://asdfsdfjasd.e-shebao.com/upload/pdfhetong/qt/411528199404087010_ht.pdf"
    }
    params = json.dumps(params)
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json',
               "host": '118.26.173.72'}
    # 用bytes函数转换为字节
    params = bytes(params, 'utf8')

    req = request.Request(url=url, data=params, headers=headers, method='POST')
    response = request.urlopen(req).read().decode()
    return json.loads(response)