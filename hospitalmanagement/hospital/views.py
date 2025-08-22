from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment, Billing, Patient, Doctor, Profile, Prescription


# --------------------------
# PATIENTS
# --------------------------
@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "hospital/patient_list.html", {"patients": patients})


# --------------------------
# DOCTORS
# --------------------------
@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "hospital/doctor_list.html", {"doctors": doctors})


# --------------------------
# APPOINTMENTS
# --------------------------
@login_required
def appointment_list(request):
    appointments = Appointment.objects.select_related("patient__user", "doctor__user")
    return render(request, "hospital/appointment_list.html", {"appointments": appointments})


# --------------------------
# BILLING
# --------------------------
@login_required
def billing_list(request):
    bills = Billing.objects.select_related("patient__user", "doctor__user")
    return render(request, "hospital/billing_list.html", {"bills": bills})
# ---- Profile Views ----
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "hospital/profile_list.html", {"profiles": profiles})


# ---- Prescription Views ----
def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, "hospital/prescription_list.html", {"prescriptions": prescriptions})




def dashboard(request):
    total_doctors = Doctor.objects.count()
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()
    total_bills = Billing.objects.count()

    return render(request, 'hospital/dashboard.html', {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'total_bills': total_bills,
    })