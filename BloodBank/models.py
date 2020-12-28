from django.db import models

class donor(models.Model):
    D_ID=models.CharField(primary_key=True, max_length=50)  ###################################email
    FNAME=models.CharField(max_length=50)
    LNAME=models.CharField(max_length=50)
    AGE=models.IntegerField()
    GENDER=models.CharField(max_length=50)
    PHONE=models.CharField(max_length=50)
    RHFACTOR=models.CharField(max_length=50)
    BLOODTYPE=models.CharField(max_length=50)
    HOUSENAME=models.CharField(max_length=50)
    STREETNAME=models.CharField(max_length=50)
    PIN=models.IntegerField()
    AADHARNO=models.IntegerField()
    LDOFDON=models.DateField(auto_now=False, auto_now_add=False)  #last date of donation #################   NULL
    PASSWORD=models.CharField(max_length=50)
    EMAIL=models.CharField(max_length=50)
    WANT_TO_DONATE=models.CharField(max_length=50)    #wiling to donate blood

    class Meta:
        db_table='donor'

########################################################################

class blood(models.Model):
    B_ID=models.CharField(max_length=50,primary_key=True)
    D_ID=models.CharField(max_length=50)
    EMP_ID=models.CharField(max_length=50)
    DATE=models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table='blood'

##################################

class hospital(models.Model):
    H_ID=models.AutoField(primary_key=True)
    HNAME=models.CharField(max_length=50)  #Hospital name
    PASSWORD=models.CharField(max_length=50)
    PHONENO=models.CharField(max_length=50)

    class Meta:
        db_table='hospital'

#############################################

class storage(models.Model):
    BLOODTYPE=models.CharField(max_length=50)
    RHFACTOR=models.CharField(max_length=50)
    BLOODAMOUNT=models.CharField(max_length=50)

    class Meta:
        db_table='storage'

##############################################

class staff(models.Model):
    EMP_ID=models.AutoField(primary_key=True)
    FNAME=models.CharField(max_length=50)
    LNAME=models.CharField(max_length=50)
    PHONENO=models.CharField(max_length=50)
    HOUSENAME=models.CharField(max_length=50)
    STREETNAME=models.CharField(max_length=50)
    PIN=models.IntegerField()

    class Meta:
        db_table='staff'


##########################################################


class req_received_blood(models.Model):
    REQUEST_ID=models.CharField(max_length=50,primary_key=True)
    H_ID=models.IntegerField()
    BLOOD_BAG_NO=models.CharField(max_length=50)
    BLOODTYPE=models.CharField(max_length=50)
    RHFACTOR=models.CharField(max_length=50)
    RECEIVED_AMOUNT=models.IntegerField()
    REQUESTED_AMOUNT=models.IntegerField()

    class Meta:
        db_table='req_recived_blood'

###############################################################

class health_cond(models.Model):
    D_ID=models.CharField(max_length=50)
    CONDITION=models.CharField(max_length=50)

    class Meta:
        db_table='health_cond'

#####################################################################

class admin_table(models.Model):
    A_ID=models.CharField(max_length=50,primary_key=True)
    FNAME=models.CharField(max_length=50)
    LNAME=models.CharField(max_length=50)
    PHONE=models.CharField(max_length=50)
    PASSWORD=models.CharField(max_length=50)

    class Meta:
        db_table='admin_table'
