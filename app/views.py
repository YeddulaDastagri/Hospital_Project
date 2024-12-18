from django.shortcuts import render

# Create your views here. 

def doctor_name(render):
    return render(request,'doctor_name.html') 

def patient(request):
    return render(request,'patient.html') 
