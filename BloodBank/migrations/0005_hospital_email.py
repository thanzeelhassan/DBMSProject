# Generated by Django 3.0.7 on 2020-12-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0004_auto_20201228_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='EMAIL',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
