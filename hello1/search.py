# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def search_form(request):
    return render_to_response('search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    def add(x, y):
        if symbol=="+":
            return x + y
        elif symbol=="-":
            return x - y
        elif symbol=="*":
            return x * y
        elif symbol=="/":
            return x / y
        else:
            return 0
    if 'q' in request.GET:
        print(request.GET['q'])
        one = int(request.GET['q'])
        two = int(request.GET['a'])
        symbol = request.GET['cars']

        if one == "" and two =="":
            message = '你提交了空表单'
        else:
            key=add(one,two)
            if not key:
                message = "none"
            else:
                message = "result:" + str(key)
    else:
        message = '你提交了空表单'
    return HttpResponse(message)