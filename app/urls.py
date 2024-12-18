from app.views import *  
from django.urls import path 


urlpatterns = [
    path('doctor_name/',doctor_name,name='doctor_name'), 
    path('patient/',patient,name='patient'),
]