#import csv,io
from django.http import HttpResponse
from django.shortcuts import render,redirect
from BloodBank.models import donor,blood,hospital,storage,staff,req_received_blood,health_cond,admin_table
#from . import forms
from django.contrib.auth import logout

def home(request):
    html = render(request,'index.html')
    return html

def admin_login(request):
    if request.method=='GET':
        return render(request, 'admin_login.html')

    else:
        post = request.POST

        username = str(post['username'])
        password = str(post['password'])
        if admin_table.objects.filter(A_ID=username,PASSWORD=password).exists() :
            return render(request, 'admin_home.html')
            #return HttpResponse("Welcome Admin")
        else:
            return HttpResponse("Username and Password does not match")

def admin_home(request):
    # NEED TO DO -------------------------
    html = render(request,'admin_home.html')
    return html

def add_hospital(request):
    if request.method=='GET':
        return render(request, 'add_hos.html')

    else:
        post = request.POST
        hname = str(post['hname'])
        username = str(post['username'])
        email = str(post['email'])
        password = str(post['password'])
        phone = str(post['phone'])

        _, created = hospital.objects.update_or_create(
                H_ID=username,
                HNAME=hname,
                PHONENO=phone,
                EMAIL=email,
                PASSWORD=password,
        )

        return HttpResponse("Success")

def add_staff(request):
    if request.method=='GET':
        return render(request, 'add_staff.html')

    else:
        post = request.POST
        fname = str(post['fname'])
        lname = str(post['lname'])
        emp_id = str(post['emp_id'])
        password = str(post['password'])
        phone = str(post['phone'])
        house_name= str(post['housename'])
        street_name = str(post['streetname'])
        pin = str(post['pin'])


        _, created = staff.objects.update_or_create(
                EMP_ID=emp_id,
                FNAME=fname,
                LNAME=lname,
                PHONENO=phone,
                PASSWORD=password,
                HOUSENAME=house_name,
                STREETNAME=street_name,
                PIN=pin
        )

        return HttpResponse("Success")

def blood_storage(request):
    html = render(request,'admin_login.html')
    return html

def approve_req(request):
    html = render(request,'admin_login.html')
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

def donor_login(request):
    if request.method=='GET':
        logout(request)
        return render(request, 'donor_login.html')

    else:
        email = request.POST['email']
        password = request.POST['password']
        obj=donor.objects.filter(D_ID=email)
        if not len(obj):
            return HttpResponse("User not found")
        obj = obj[0]
        if obj.PASSWORD != password:
            return HttpResponse('Password wrong')
        request.session['email'] = email
        request.session.set_expiry(14400)
        return redirect('/donor_home/')

def donor_home(request):
    if not request.session.get('email'):
        return HttpResponse("Session Expired.")
    if request.method=='GET':
        return render(request, 'donor_home.html')
    else:
        email = request.session['email']
        obj1=donor.objects.filter(D_ID=email)
        obj2=health_cond.objects.filter(D_ID=email)
        obj1 = obj1[0]
        obj2 = obj2[0]
        will = request.POST['will']
        health = request.POST['health']
        if(will == "YES"):
            obj1.WANT_TO_DONATE = 'YES'
            obj1.save()
        if(will == 'NO'):
            obj1.WANT_TO_DONATE = 'NO'
            obj1.save()
        if(health != ""):
            obj2.CONDITION = health
            obj2.save()

        return redirect('/donor_home/')

def staff_login(request):
    if request.method=='GET':
        logout(request)
        return render(request, 'staff_login.html')

    else:
        email = request.POST['email']
        password = request.POST['password']
        obj=donor.objects.filter(D_ID=email)
        if not len(obj):
            return HttpResponse("User not found")
        obj = obj[0]
        if obj.PASSWORD != password:
            return HttpResponse('Password wrong')
        request.session['email'] = email
        request.session.set_expiry(14400)
        return redirect('/donor_home/')

def staff_home(request):
    html = render(request,'donor_home.html')
    return html

def hospital_login(request):
    html = render(request,'donor_home.html')
    return html

def hospital_home(request):
    html = render(request,'donor_home.html')
    return html
