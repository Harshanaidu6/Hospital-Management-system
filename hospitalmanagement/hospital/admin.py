from django.contrib import admin
from .models import Profile, Patient, Doctor, Appointment, Prescription, Billing


# Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)

def __str__(self):
    return self.user.username

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'age', 'gender', 'contact')
    search_fields = ('user__username', 'contact')

    def patient_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
    patient_name.short_description = "Patient Name"


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor_name', 'specialization', 'availability')
    search_fields = ('user__username', 'specialization')

    def doctor_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
    doctor_name.short_description = "Doctor Name"



# Appointment Admin
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'date', 'time', 'status')
    search_fields = ('patient__name', 'doctor__name')
    list_filter = ('status', 'date')


# Prescription Admin
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'medicines', 'dosage')
    search_fields = ('appointment__patient__name',)


# Billing Admin
@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'amount', 'status', 'date')
    list_filter = ('status', 'date')
