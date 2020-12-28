#import csv,io
from django.http import HttpResponse
from django.shortcuts import render,redirect
from BloodBank.models import donor,blood,hospital,storage,staff,req_received_blood,health_cond,admin_table
#from . import forms
#from django.contrib.auth import logout

def home(request):
    html = render(request,'index.html')
    return html

def donor_reg(request):
    if request.method=='GET':
        return render(request, 'donor_reg.html')

    else:
        post = request.POST

        fname = str(post['fname'])
        lname = str(post['lname'])
        age = str(post['age'])
        email = str(post['email'])
        password = str(post['password'])
        c_password = str(post['c_password'])
        phone = str(post['phone'])
        blood = str(post['blood'])
        rh = str(post['rh'])
        house = str(post['house'])
        street = str(post['street'])
        pin = str(post['pin'])
        aadhar = str(post['aadhar'])
        gender = str(post['gender'])

        if(password != c_password):
            return HttpResponse("Password mismatch")

        _, created = donor.objects.update_or_create(
                D_ID=email,
                FNAME=fname,
                LNAME=lname,
                AGE=age,
                GENDER=gender,
                PHONE=phone,
                RHFACTOR=rh,
                BLOODTYPE=blood,
                HOUSENAME=house,
                STREETNAME=street,
                PIN=pin,
                AADHARNO=aadhar,
                LDOFDON='1999-03-03',  #last date of donation #############
                PASSWORD=password,
                #NOTIFICATION_EID=models.CharField(max_length=50)
                EMAIL=email,
                WANT_TO_DONATE='1998-02-02', ##############
            )

        return HttpResponse("Success")

def admin_login(request):
    html = render(request,'admin_login.html')
    return html

def login_page(request):
    html = render(request,'admin_login.html')
    return html

def staff_page(request):
    html = render(request,'staff_home.html')
    return html

def hospital_page(request):
    html = render(request,'hos_home.html')
    return html

def admin_page(request):
    html = render(request,'admin_home.html')
    return html

def add_hospital(request):
    html = render(request,'add_hos.html')
    return html

def add_staff(request):
    html = render(request,'add_staff.html')
    return html

def blood_storage(request):
    html = render(request,'admin_login.html')
    return html

def approve_req(request):
    html = render(request,'admin_login.html')
    return html

def donor_page(request):
    html = render(request,'donor_home.html')
    return html
