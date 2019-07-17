from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def mysum(request, numbers):
    #numbers = "1/12/123/12/123"
    result = sum(map(lambda s : int(s or 0), numbers.split("/")))
    return HttpResponse(result)