from django.shortcuts import render,redirect
from app1.forms import DoctorForm,PatientForm,AppointmentForm
from app1.models import Doctor,Patient,Appointment
from django.urls import reverse
# Create your views here.

#doctors dedails added here
def doctoradd(request):
    mesg=''
    if request.method=='POST':
        d=DoctorForm(request.POST)
        if d.is_valid():
            d.save()
            mesg="doctor details Added"
    form=DoctorForm()
    response=render(request,'adddoctor.html',context={'form':form,'mesg':mesg})
    return response

#this is for list of doctor 
def listdoctors(request):
    qs=Doctor.objects.all()
    response=render(request,"listdoctors_temp.html",context={'qs':qs})
    return response



#this ia for home page
def home(request):
    response=render(request,'base.html',context={})
    return response

def doctoredit(request,name):
    d=Doctor.objects.get(name=name)
    if request.method=='POST':
        form=DoctorForm(request.post,instance=d)
        if form.is_valid():
            form.save()
            response=redirect('doctorlist')
            return response
    form=DoctorForm(instance=d)
    
def patientlist(request):
    qs=Patient.objects.all()
    res=render(request,'listpatient_temp.html',context={'qs':qs})
    return res

def patientadd(request):
    msg=""
    if request.method == "POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Patient Details Added sucssesfuly"



