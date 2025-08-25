from django.forms import ModelForm
from app1.models import Doctor,Patient,Appointment
class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields='__all__' 
class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'
        