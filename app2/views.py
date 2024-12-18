from django.shortcuts import render

# Create your views here. 

def appointment(request):
    return render(render,'appointment.html') 
def patient_bill(request):
    return render(request,'patient_bill.html')

