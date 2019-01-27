from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def teacher(request):
    return HttpResponse('THIS TEACHER VIEWS')
def v2_exception(request):
    raise Http404
    return HttpResponse('OK')
