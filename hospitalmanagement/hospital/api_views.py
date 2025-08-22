from rest_framework import generics
from .models import Patient, Appointment
from .serialzier import PatientSerializer, AppointmentSerializer

class PatientListAPI(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentListAPI(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
