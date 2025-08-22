from django.contrib import admin
from django.urls import path
from hospital import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard
    path("", views.dashboard, name="dashboard"),
    
    path('dashboard/', views.dashboard, name='dashboard'),


    # Patients
    path("patient_list/", views.patient_list, name="patient_list"),

    # Doctors
    path("doctor_list/", views.doctor_list, name="doctor_list"),

    # Appointments
    path("appointment_list/", views.appointment_list, name="appointment_list"),

    # Billing
    path("billing_list/", views.billing_list, name="billing_list"),

    # Profiles
    path("profile_list/", views.profile_list, name="profile_list"),

    # Prescriptions
    path("prescription_list/", views.prescription_list, name="prescription_list"),
   
]
