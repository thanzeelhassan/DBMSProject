# Generated by Django 3.0.7 on 2020-12-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0007_auto_20201228_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='PASSWORD',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]