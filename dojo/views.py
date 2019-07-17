from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def mysum(request, x, y=0, z=0):
    print(x,y,z)
    return HttpResponse(int(x) + int(y) + int(z))