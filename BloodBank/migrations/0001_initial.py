# Generated by Django 3.0.7 on 2020-12-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('A_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('FNAME', models.CharField(max_length=50)),
                ('LNAME', models.CharField(max_length=50)),
                ('PHONE', models.IntegerField()),
                ('PASSWORD', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='blood',
            fields=[
                ('B_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('D_ID', models.IntegerField()),
                ('EMP_ID', models.CharField(max_length=50)),
                ('DATE', models.DateField()),
            ],
            options={
                'db_table': 'blood',
            },
        ),
        migrations.CreateModel(
            name='donor',
            fields=[
                ('D_ID', models.AutoField(primary_key=True, serialize=False)),
                ('FNAME', models.CharField(max_length=50)),
                ('LNAME', models.CharField(max_length=50)),
                ('AGE', models.IntegerField()),
                ('GENDER', models.CharField(max_length=50)),
                ('PHONE', models.IntegerField()),
                ('RHFACTOR', models.CharField(max_length=50)),
                ('BLOODTYPE', models.CharField(max_length=50)),
                ('HOUSENAME', models.CharField(max_length=50)),
                ('STREETNAME', models.CharField(max_length=50)),
                ('PIN', models.IntegerField()),
                ('AADHARNO', models.IntegerField()),
                ('LDOFDON', models.DateField()),
                ('PASSWORD', models.CharField(max_length=50)),
                ('NOTIFICATION_EID', models.CharField(max_length=50)),
                ('EMAIL', models.CharField(max_length=50)),
                ('WANT_TO_DONATE', models.DateField()),
            ],
            options={
                'db_table': 'donor',
            },
        ),
        migrations.CreateModel(
            name='health_cond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_ID', models.IntegerField()),
                ('CONDITION', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'health_cond',
            },
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('H_ID', models.AutoField(primary_key=True, serialize=False)),
                ('HNAME', models.CharField(max_length=50)),
                ('PASSWORD', models.CharField(max_length=50)),
                ('PHONENO', models.IntegerField()),
            ],
            options={
                'db_table': 'hospital',
            },
        ),
        migrations.CreateModel(
            name='req_recived_blood',
            fields=[
                ('REQUEST_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('H_ID', models.IntegerField()),
                ('BLOOD_BAG_NO', models.CharField(max_length=50)),
                ('BLOODTYPE', models.CharField(max_length=50)),
                ('RHFACTOR', models.CharField(max_length=50)),
                ('RECIVED_AMOUNT', models.IntegerField()),
                ('REQUESTED_AMOUNT', models.IntegerField()),
            ],
            options={
                'db_table': 'req_recived_blood',
            },
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('EMP_ID', models.AutoField(primary_key=True, serialize=False)),
                ('FNAME', models.CharField(max_length=50)),
                ('LNAME', models.CharField(max_length=50)),
                ('PHONENO', models.IntegerField()),
                ('HOUSENAME', models.CharField(max_length=50)),
                ('STREETNAME', models.CharField(max_length=50)),
                ('PIN', models.IntegerField()),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BLOODTYPE', models.CharField(max_length=50)),
                ('RHFACTOR', models.CharField(max_length=50)),
                ('BLOODAMOUNT', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'storage',
            },
        ),
    ]
