from django.contrib import admin
from django.urls import include, path
from BloodBank import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('login_page', views.login_page, name= 'login_page'),
    path('hospital_page/', views.hospital_page, name='hospital_page'),
    path('admin_page', views.admin_page, name= 'admin_page'),
    path('add_hospital/', views.add_hospital, name='add_hospital'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('blood_storage/', views.blood_storage, name= 'blood_storage'),
    path('approve_req/', views.approve_req, name='approve_req'),
    
    path('donor_reg/', views.donor_reg, name='donor_reg'),
    path('donor_login/', views.donor_login, name='donor_login'),
    path('donor_home/', views.donor_home, name='donor_home'),
    path('', views.index, name='index'),
    path('staff_home/', views.staff_home, name='staff_home'),
    path('staff_login/', views.staff_login, name='staff_home'),
]
