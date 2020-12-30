#import csv,io
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render,redirect
from BloodBank.models import donor,blood,hospital,storage,staff,req_received_blood,health_cond,admin_table
#from . import forms
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    if request.method=='GET':
        logout(request)
        return render(request, 'admin_login.html')

    else:
        post = request.POST
        username = request.POST['username']
        password = request.POST['password']
        if admin_table.objects.filter(A_ID=username,PASSWORD=password).exists() :
            request.session['username'] = username
            request.session.set_expiry(14400)
            return redirect('/admin_home/')
        else:
            return HttpResponse("Username and Password does not match")

def admin_home(request):
    return render(request,'admin_home.html')

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
        address=str(post['address'])
        pin=str(post['pin'])

        _, created = hospital.objects.update_or_create(
                H_ID=username,
                HNAME=hname,
                PHONENO=phone,
                EMAIL=email,
                PASSWORD=password,
                ADDRESS=address,
                PIN=pin
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
    var1=storage.objects.values().order_by('BLOODTYPE')
    list_result = [entry for entry in var1]
    return render(request,'blood_storage.html',{'abcd2':list_result})

def approve_req(request):
    var1=req_received_blood.objects.values()
    list_result = [entry for entry in var1]
    #request.session['request_id'] =
    return render(request,'approve_req.html',{'abcd2':list_result})

def approve(request):
    var2 = request.POST.get('request_id',None)
    var4 = request.POST.get('requested_amount',None)

    var3 =req_received_blood.objects.get(REQUEST_ID=var2)
    var3.RECEIVED_AMOUNT = var4
    var3.save()

    var1=req_received_blood.objects.values()
    list_result = [entry for entry in var1]
    return render(request,'approve.html',{'abcd2':list_result})

def reject(request):
    var2 = request.POST.get('request_id',None)
    entry = req_received_blood.objects.get(REQUEST_ID = var2)
    entry.delete()
    #req_received_blood.objects.filter(REQUEST_ID=var2).delete()
    var1=req_received_blood.objects.values()
    list_result = [entry for entry in var1]
    return render(request,'approve.html',{'abcd2':list_result})

def admin_search(request):
    var2 = request.POST.get('donor_id',None)
    var2 ="Thanzeel47"
    var1 = donor.objects.get(D_ID = var2)
    return render(request,'admin_search.html',{'abcd2':var1})

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
                WANT_TO_DONATE='YES', ##############
            )
        _, created = health_cond.objects.update_or_create(
                D_ID = email,
                CONDITION = "",
            )

        return redirect('/donor_login/')

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
        return HttpResponse("Session Expired. Please Login Again.")
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
        username = request.POST['username']
        password = request.POST['password']
        obj=staff.objects.filter(EMP_ID=username)
        if not len(obj):
            return HttpResponse("User not found")
        obj = obj[0]
        if obj.PASSWORD != password:
            return HttpResponse('Password wrong')
        request.session['username'] = username
        request.session.set_expiry(14400)
        return redirect('/staff_home/')

def staff_home(request):
    if not request.session.get('username'):
        return HttpResponse("Session Expired.")
    if request.method=='GET':
        return render(request, 'staff_home.html')
    else:
        username = request.session['username']
        b_id = request.POST['b_id']
        d_id = request.POST['d_id']
        blood_type = request.POST['blood_type']
        rh_factor = request.POST['rh_factor']
        blood_amount = request.POST['blood_amount']
        date = request.POST['DATE']
        donor_obj = donor.objects.filter(D_ID=d_id)
        donor_obj = donor_obj[0]
        _, created = blood.objects.update_or_create(
                B_ID=b_id,
                D_ID=d_id,
                BLOODTYPE=blood_type,
                RHFACTOR=rh_factor,
                BLOODAMOUNT=blood_amount,
                EMP_ID=username,
                DATE=date,
        )
        if str(date) > str(donor_obj.LDOFDON):
            donor_obj.LDOFDON = date
            donor_obj.save()

        storage_obj = storage.objects.filter(BLOODTYPE=blood_type,RHFACTOR=rh_factor)
        if not len(storage_obj):
            _, created = storage.objects.update_or_create(
                BLOODTYPE=blood_type,
                RHFACTOR=rh_factor,
                BLOODAMOUNT=blood_amount,
            )
        else:
            storage_obj = storage_obj[0]
            storage_obj.BLOODAMOUNT = str( int(storage_obj.BLOODAMOUNT) + int(blood_amount) )
            storage_obj.save()

        return redirect('/staff_home/')

def hospital_login(request):
    if request.method=='GET':
        logout(request)
        return render(request, 'hospital_login.html')

    else:
        username = request.POST['username']
        password = request.POST['password']
        obj=hospital.objects.filter(H_ID=username)
        if not len(obj):
            return HttpResponse("Hospital not found")
        obj = obj[0]
        if obj.PASSWORD != password:
            return HttpResponse('Password wrong')
        request.session['username'] = username
        request.session.set_expiry(14400)
        return redirect('/hospital_home/')

def hospital_home(request):
    if not request.session.get('username'):
        return HttpResponse("Session Expired.")
    if request.method=='GET':
        return render(request,'hospital_home.html')
    else:
        username = request.session['username']
        b_group = request.POST['b_group']
        rh = request.POST['rh']
        amount = request.POST['amount']
        request_id = username + '_' +b_group + '_' + rh + '_' + str(date.today())

        _, created = req_received_blood.objects.update_or_create(
                REQUEST_ID=request_id,
                H_ID=username,
                BLOOD_BAG_NO='0',
                BLOODTYPE=b_group,
                RHFACTOR=rh,
                RECEIVED_AMOUNT=0,
                REQUESTED_AMOUNT=amount,
        )

        return redirect('/hospital_home/')
