from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
'''
视图函数需要一个参数，类型应该是HttpRequest参数
'''

# 普通
def do_nomalmap(request):
    return HttpResponse('This is normalmap')
# 带参数
def withparam(request, year, month):
    return HttpResponse('THIS IS {0},{1}'.format(year, month))

def do_xiaolin(request):
    return HttpResponse('THIS IS XIAOLIN PAGE')
def do_book(request, pagenumber):
    return HttpResponse('THIS IS {0} DO_BOOK'.format(pagenumber))
# 额外参数
def do_param(request, name):
    return HttpResponse('THIS IS MY {}'.format(name))

# 反向解析
def revParse(request):
    print(request)
    return HttpResponse('this is {}'.format(reverse('aaa')))





                        






