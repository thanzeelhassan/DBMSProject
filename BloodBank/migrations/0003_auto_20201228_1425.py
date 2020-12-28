# Generated by Django 3.0.7 on 2020-12-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0002_auto_20201228_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='NOTIFICATION_EID',
        ),
        migrations.AlterField(
            model_name='blood',
            name='D_ID',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='donor',
            name='D_ID',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='health_cond',
            name='D_ID',
            field=models.CharField(max_length=50),
        ),
    ]