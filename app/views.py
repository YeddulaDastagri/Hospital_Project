from django.shortcuts import render

# Create your views here. 

def cardiologist(render):
    return render(request,'cardiologist.html') 

def dermatologist(request):
    return render(request,'dermatologist.html') 
