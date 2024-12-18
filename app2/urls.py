from app2.views import *  
from django.urls import path 


urlpatterns = [
    path('appointment/', appointment,name='appointment'), 
    path('patient_bill/',patient_bill,name='patient_bill'),
]