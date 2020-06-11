#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from hf.view.p2pMysql import createDbCon


def withDrawalSuccess(idCardNo,cashAmount,recordNo):
    response_data = {}
    response_data['Success'] = True
    response_data['Code'] = "0"
    response_data['Message'] = "FF成功"
    cursor = createDbCon()
    sql = '''SELECT user_name,user_bank_no FROM psp_bank_card 
    WHERE user_id_no='''+idCardNo+''' GROUP BY user_id_no;'''
    data = {}
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        data['full_name'] = str(row[0])
        data['user_bank_account'] = str(row[1])
    data['id_card_no']=idCardNo
    data['user_accout_ye'] =100000000
    data['tax'] =float(cashAmount)*0.1
    data['cash_amount'] = float(cashAmount)
    data['tax_income'] =float(cashAmount)-data['tax']
    data['record_no'] =recordNo
    response_data['Data'] = data
    return response_data
def withDrawalFalse(recordNo):
    response_data = {}
    response_data['Success'] = False
    response_data['Message'] = "失败"
    response_data['Code'] = "1001"
    data = {}
    data['msg'] = "FF验证未通过"
    data['record_no'] = recordNo
    response_data['Data'] = data
    return response_data

