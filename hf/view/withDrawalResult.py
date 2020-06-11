#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from urllib import request
from hf.view.p2pMysql import createDbCon
from time import strftime,gmtime
from hf.view.getConfig import getHfWithDrawManualResult

def withDrawalResultSuccess(recordNo):

    url = getHfWithDrawManualResult()
    cursor = createDbCon()
    sql = '''SELECT id_card_no,amount FROM psp_hf_transfer WHERE record_no="''' + recordNo + '''";'''
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        idCardNo = str(row[0])
        amount = str(row[1])
    tax=float(amount)*0.1
    taxIncome=float(amount)-tax
    tansTime=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    params = {
        "record_no":recordNo,
        "detail_pay_state":2,
        "user_bank_account":"",
        "user_accout_ye":"1000000000",
        "cash_amount":amount,
        "tax_income":taxIncome,
        "tax":tax ,
        "transaction_time":tansTime,
        "fail_reason": "FF转账成功",
        "full_name":"",
        "id_card_no":idCardNo
    }
    params = json.dumps(params)
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
    # 用bytes函数转换为字节
    params = bytes(params, 'utf8')

    req = request.Request(url=url, data=params, headers=headers, method='POST')
    response = request.urlopen(req).read().decode()
    return json.loads(response)

def withDrawalResultFalse(recordNo):
    url = getHfWithDrawManualResult()
    cursor = createDbCon()
    sql = '''SELECT id_card_no,amount FROM psp_hf_transfer WHERE record_no="''' + recordNo + '''";'''
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        idCardNo = str(row[0])
        amount = str(row[1])
    tax = float(amount) * 0.1
    taxIncome = float(amount) - tax
    tansTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    params = {
        "record_no": recordNo,
        "detail_pay_state": 3,
        "user_bank_account": "",
        "user_accout_ye": "1000000000",
        "cash_amount": amount,
        "tax_income": taxIncome,
        "tax": tax,
        "transaction_time": tansTime,
        "fail_reason": "FF转账失败-银行验证不通过",
        "full_name": "",
        "id_card_no": idCardNo
    }
    params = json.dumps(params)
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
    # 用bytes函数转换为字节
    params = bytes(params, 'utf8')

    req = request.Request(url=url, data=params, headers=headers, method='POST')
    response = request.urlopen(req).read().decode()
    return json.loads(response)