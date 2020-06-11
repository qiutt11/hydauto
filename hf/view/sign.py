#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

#签约申请状态
def signSuccess():
    response_data = {}
    response_data['Success'] = True
    response_data['Message'] = "成功"
    response_data['Data'] = "请等待人工审核，预计1个工作日（会有短信提醒）"
    return response_data
def signFalse():
    response_data = {}
    response_data['Success'] = False
    response_data['Message'] = "失败"
    response_data['Code'] = "2005"
    response_data['Data'] = "fl原因是手机号和身份证号在黑名单中"
    return response_data