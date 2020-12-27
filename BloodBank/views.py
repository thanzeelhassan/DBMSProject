#import csv,io
from django.http import HttpResponse
from django.shortcuts import render,redirect
from BloodBank.models import donor,blood,hospital,storage,staff,req_recived_blood,health_cond,admin
#from . import forms
#from django.contrib.auth import logout

def home(request):
    html = render(request,'index.html')
    return html
