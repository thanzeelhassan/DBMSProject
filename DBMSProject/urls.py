from django.contrib import admin
from django.urls import include, path
from BloodBank import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name= 'admin_home'),
    path('add_hospital/', views.add_hospital, name='add_hospital'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('blood_storage/', views.blood_storage, name= 'blood_storage'),
    path('approve_req/', views.approve_req, name='approve_req'),

    path('donor_reg/', views.donor_reg, name='donor_reg'),
    path('donor_login/', views.donor_login, name='donor_login'),
    path('donor_home/', views.donor_home, name='donor_home'),

    path('staff_home/', views.staff_home, name='staff_home'),
    path('staff_login/', views.staff_login, name='staff_login'),

    path('hospital_login/', views.hospital_login, name='hospital_home'),
    path('hospital_home/', views.hospital_home, name='hospital_page'), 
]
