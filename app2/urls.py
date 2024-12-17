from app2.views import *  
from django.urls import path 


urlpatterns = [
    path('neurologist/', neurologist,name='neurologist'), 
    path('therapist/',therapist,name='therapist'),
]