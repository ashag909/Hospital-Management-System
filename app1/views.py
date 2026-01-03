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

def doctordelete(request,name):
    qs=Doctor.objects.filter(name=name)
    qs.delete()
    res=redirect("doctorlist")
    return res

def doctoredit(request,name):
    doctor_edit=Doctor.objects.get(name=name)
    if request.method=='POST':
        form=DoctorForm(request.post,instance=doctor_edit) # instance means you are editing an existing object (row) instead of creating a new one.
        if form.is_valid():
            form.save()
            response=redirect('doctorlist')
            return response
    form=DoctorForm(instance=doctor_edit)

#this is for home page
def home(request):
    response=render(request,'base.html',context={})
    return response

def patientadd(request):
    msg=""
    if request.method == "POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Patient Details Added sucssesfuly"
    form=PatientForm()
    res=render(request,"patientadd_temp.html",context={'form':form,'msg':msg})
    return res

def patientlist(request):
    qs=Patient.objects.all()
    res=render(request,'listpatient_temp.html',context={'qs':qs})
    return res

def patientedit(request,name):
    patient_edit=Patient.objects.get(name=name)
    if request.method=="POST":
        form=PatientForm(request.POST,instance=patient_edit)
        if form.is_valid():
            form.save()
            response=redirect("patientlist")
            return response
    form=PatientForm(instance=patient_edit)
    response=redirect(request,"editpatient_temp.html",context={'form':form})
    return response

def patientdelete(request,name):
    patient_del=Patient.objects.get(name=name)
    patient_del.delete()
    response=redirect('patientlist')
    return response



def appointment(request):
    msg=""
    if request.method =="POST":
        d=Doctor.objects.get(name=request.POST.get('doctor'))
        p=Patient.objects.get(name=request.POST.get('patient'))
        date=request.POST.get('date')
        time=request.POST.get('time')
        desc=request.POST.get('desc')
        Appointment.objects.create(doctor=d,patient=p,date=date,time=time,description=desc)
        msg=""
