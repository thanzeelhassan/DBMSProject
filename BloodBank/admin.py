from django.contrib import admin
from BloodBank.models import donor,blood,hospital,storage,staff,req_received_blood,health_cond,admin_table

admin.site.register(donor)
admin.site.register(blood)
admin.site.register(hospital)
admin.site.register(storage)
admin.site.register(staff)
admin.site.register(req_received_blood)
admin.site.register(health_cond)
admin.site.register(admin_table)
