#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from hf.view.sign import signSuccess,signFalse
from hf.view.withDrawal import withDrawalSuccess,withDrawalFalse
from hf.view.autograph import autographsuccess
from hf.view.signResult import resultSuccess,resultFalse
from hf.view.withDrawalResult import withDrawalResultSuccess,withDrawalResultFalse
import json
# Create your views here.

def index(request):

    return render(request,"index.html")
def callback(request):

    return render(request,"callBack.html")


#慧发签约
def sign(request):

    useName =json.loads(request.body)['params']['full_name']
    if (useName.startswith('成',0)):
        response_data=signSuccess()
    elif (useName.startswith('败',0)):
        response_data = signFalse()
    else:
        response_data = signSuccess()
    return JsonResponse(response_data)

#转账申请
def withDrawal(request):

    print(json.loads(request.body))
    idCardNo = json.loads(request.body)['params']['id_card_no']
    cashAmount = json.loads(request.body)['params']['cash_amount']
    recordNo = json.loads(request.body)['params']['record_no']
    if (float(cashAmount)<=1000):
        response_data = withDrawalSuccess(idCardNo,cashAmount,recordNo)
    else:
        response_data=withDrawalFalse(recordNo)
    return JsonResponse(response_data)

#模拟签字
def autograph(request):

    phoneNumber = request.GET.get('phone_number','')
    idCardNo = request.GET.get('id_card_no','')
    #idCardNo = json.loads(request.body)['id_card_no']
    #phoneNumber = json.loads(request.body)['phone_number']
    response_data = autographsuccess(idCardNo,phoneNumber)
    print(response_data)
    return JsonResponse(response_data)

#签约审核
def signResult(request):
    idCardNo=request.POST.get('idcard')
    result=int(request.POST.get('review'))
    print(idCardNo)
    print(result)
    if result==1:
        response_data = resultSuccess(idCardNo,result)
        print(response_data)
        if response_data['Success'] == "true":
            return HttpResponse("审核成功")
        else:
            return HttpResponse("审核成功通知失败")
    else:
        response_data = resultFalse(idCardNo, result)
        print(response_data)
        if response_data['Success'] == "true":
            return HttpResponse("审核失败")
        else:
            return HttpResponse("审核失败通知失败")

#查询授权报税委托书
def getContract(request):

    response_data = {}
    response_data['Success'] = True
    response_data['Message'] = "成功"
    response_data['Data'] = "https://tshf.api.huibanshe.com/upload/ht_pdf/171355e620d34a6f9a2b8a6a53f73a26.pdf"
    return JsonResponse(response_data)


#转账结果
def withDrawalResult(request):
    recordNo=str(request.POST.get('recordNo'))
    result=int(request.POST.get('review'))
    print(recordNo)
    print(result)
    if result==2:
        response_data = withDrawalResultSuccess(recordNo)
        print(response_data)
        if response_data['Data'] == "1":
            return HttpResponse("转账成功")
        else:
            return HttpResponse("转账成功通知失败")
    else:
        response_data = withDrawalResultFalse(recordNo)
        print(response_data)
        if response_data['Data'] == "1":
            return HttpResponse("转账失败")
        else:
            return HttpResponse("转账失败通知失败")
