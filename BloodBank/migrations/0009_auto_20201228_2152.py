# Generated by Django 3.0.7 on 2020-12-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0008_staff_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood',
            name='BLOODAMOUNT',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blood',
            name='BLOODTYPE',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blood',
            name='RHFACTOR',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
