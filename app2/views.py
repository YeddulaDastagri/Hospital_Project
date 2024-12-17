from django.shortcuts import render

# Create your views here. 

def neurologist(request):
    return render(render,'neurologist.html') 
def therapist(request):
    return render(request,'therapist')

